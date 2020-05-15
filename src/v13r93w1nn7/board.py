import numpy as np

ROWS = 6
COLS = 7

EMPTY = 0
PLAYER_ONE = 1
PLAYER_TWO = 2

FIELD_VALUES = [EMPTY, PLAYER_ONE, PLAYER_TWO]


class Board:

    def __init__(self, b=None):
        if b is not None:
            self.b = b
        else:
            self.b = np.zeros((ROWS, COLS), dtype=np.byte)

    @staticmethod
    def from_list(l):
        np_arr = np.array(l)
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
