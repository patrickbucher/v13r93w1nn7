import numpy as np

ROWS = 6
COLS = 7

EMPTY = 0
PLAYER_ONE = 1
PLAYER_TWO = 2
NEUTRAL = 3

FIELD_VALUES = [EMPTY, PLAYER_ONE, PLAYER_TWO, NEUTRAL]

SHIFTS = {
    # direction: (row shift, col shift)
    'north': (-1, 0),
    'north_east': (-1, 1),
    'east': (0, 1),
    'south_east': (1, 1),
    'south': (1, 0),
    'south_west': (1, -1),
    'west': (0, -1),
    'north_west': (-1, -1),
}


class Board:

    def __init__(self, b=None):
        if b is not None:
            self.b = b
        else:
            self.b = np.zeros((ROWS, COLS), dtype=np.byte)

    @staticmethod
    def from_list(lst, validate=True):
        np_arr = np.array(lst)
        if validate:
            if np_arr.shape[0] != ROWS or np_arr.shape[1] != COLS:
                raise ValueError(f'shape must be {ROWS}x{COLS}')
            ok = np.all(np.isin(np_arr, FIELD_VALUES))
            if not ok:
                raise ValueError(f'only values {FIELD_VALUES} allowed')
        return Board(b=np_arr)

    def rows(self):
        return self.b.shape[0]

    def cols(self):
        return self.b.shape[1]

    def as_list(self):
        return self.b.tolist()

    def valid_moves(self):
        empty_at = np.argwhere(self.b[0] == EMPTY).flatten()
        return empty_at.tolist()

    def apply_move(self, player, move):
        if move not in self.valid_moves():
            raise ValueError(f'{move} is not a valid move')
        col = self.b.transpose()[move]
        row_index = np.amax(np.argwhere(col == EMPTY).flatten())
        new_b = np.copy(self.b)
        new_b[row_index, move] = player
        return Board(new_b)

    def is_draw(self):
        return not np.any(self.b == EMPTY)

    def wins(self):
        # Rotating the field could result in multiple wins. The winning fields
        # should also be highlighted and are therefore returned.
        four_in_a_row = {
            PLAYER_ONE: [],
            PLAYER_TWO: [],
        }
        for row in range(self.b.shape[0]):
            for col in range(self.b.shape[1]):
                player = self.b[row, col]
                if player in [EMPTY, NEUTRAL]:
                    continue
                for direction in SHIFTS.values():
                    win_indices = self.is_win(player, (row, col), direction)
                    if win_indices:
                        if sorted(win_indices) in four_in_a_row[player]:
                            continue
                        four_in_a_row[player].append(sorted(win_indices))
        four_in_a_row[PLAYER_ONE] = sorted(four_in_a_row[PLAYER_ONE])
        four_in_a_row[PLAYER_TWO] = sorted(four_in_a_row[PLAYER_TWO])
        return four_in_a_row

    def is_win(self, player, orig, direction):
        matches = []
        row, col = orig[0], orig[1]
        while 0 <= row < self.b.shape[0] and 0 <= col < self.b.shape[1]:
            if self.b[row, col] == player:
                matches.append((row, col))
            else:
                return None
            if len(matches) >= 4:
                return matches
            row, col = row + direction[0], col + direction[1]
        return None

    def draw(self, indent='\t', p1='x', p2='o',
             empty='_', illegal='?', slotnums=False):
        fields = {
            EMPTY: empty,
            PLAYER_ONE: p1,
            PLAYER_TWO: p2,
        }
        output = ''
        if slotnums:
            slots = [i for i in range(1, self.cols() + 1)]
            line = indent
            for slot in slots:
                line += f'{slot} '
            output += line.rstrip() + '\n'
        for r in range(self.rows()):
            line = indent
            for c in range(self.cols()):
                if self.b[r, c] in fields:
                    f = fields[self.b[r, c]]
                    line += f'{f} '
                else:
                    line += f'{illegal} '
            output += line.rstrip() + '\n'
        return output
