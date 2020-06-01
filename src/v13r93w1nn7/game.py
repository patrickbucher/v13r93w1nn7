#!/usr/bin/env python3

import argparse
import random
import os

from board import Board, CLOCKWISE, COUNTER_CLOCKWISE


def main(neutral=False, rotate=False):
    b = Board()
    p1, p2, pn = (1, 'x', 'X'), (2, 'o', 'O'), (3, '.', '.')
    finished = False
    p = p1
    draw = decorate_draw(
        p1=p1[1],
        p2=p2[1],
        pn=pn[1],
        empty='_',
        slotnums=True)
    while not finished:
        if neutral and p == p1:
            # put neutral stone before p1 plays (before every round)
            moves = b.valid_moves()
            if moves:
                b = b.apply_move(pn[0], random.choice(moves))
            if b.is_draw():
                end_draw(b, draw)
                break
        clear()
        print(draw(b))
        played = False
        while not played:
            lower, upper = 1, b.cols()
            prompt = build_prompt(p, lower, upper, rotate)
            entered = input(prompt) + ''
            entered = entered.strip().lower()
            if rotate and entered == 'rr':
                b = b.rot90(CLOCKWISE)
                played = True
            elif rotate and entered == 'rl':
                b = b.rot90(COUNTER_CLOCKWISE)
                played = True
            else:
                try:
                    slot = int(entered)
                    if lower <= slot <= upper and (slot-1) in b.valid_moves():
                        b = b.apply_move(p[0], slot-1)
                        played = True
                    else:
                        wrong_move(lower, upper, rotate)
                except ValueError:
                    wrong_move(lower, upper, rotate)
        wins = b.wins()
        opponent = p2 if p == p1 else p1
        if wins[p[0]]:
            end_win(b, draw, p, wins)
            finished = True
        elif wins[opponent[0]]:
            end_win(b, draw, opponent, wins)
            finished = True
        elif b.is_draw():
            end_draw(b, draw)
            finished = True
        p = p2 if p == p1 else p1


def end_draw(b, draw):
    clear()
    print(draw(b))
    print('The game ended in a draw.')


def end_win(b, draw, player, wins):
    clear()
    coords = wins[player[0]][0]
    winner_board = highlight_winner(b, draw, coords, player[2])
    print(winner_board)
    print(f'Player {player[0]} has won the game.')


def build_prompt(player, lower, upper, rotate):
    prompt = f'Player {player[0]} [{player[1]}] '
    if rotate:
        prompt += f'({lower} to {upper}, rr/rl for rotation): '
    else:
        prompt += f'({lower} to {upper}): '
    return prompt


def highlight_winner(b, draw, coords, new):
    winner_board = b.as_list()
    for f in coords:
        winner_board[f[0]][f[1]] = 9  # dummy value
    new_b = Board.from_list(winner_board, validate=False)
    output = draw(new_b)
    return output.replace('?', new)


def wrong_move(lower, upper, rotate=False):
    msg = f'You must pick a free slot between {lower} and {upper}'
    if rotate:
        msg += ', or rr/rl to rotate!'
    else:
        msg += '!'
    print(msg)


def decorate_draw(p1, p2, pn, empty, slotnums):
    def _draw(b):
        return b.draw(p1=p1, p2=p2, pn=pn, empty=empty, slotnums=slotnums)
    return _draw


def clear():
    if os.name == 'nt':
        # Windows
        os.system('cls')
    else:
        # Unix
        os.system('clear')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='v13r93w1nn7')
    parser.add_argument(
        '--neutral', default=False, action='store_true',
        help='enable neutral stones falling randomly before every round')
    parser.add_argument(
        '--rotate', default=False, action='store_true',
        help='enable rotation (clockwise and counter clockwise)')
    args = parser.parse_args()
    main(neutral=args.neutral, rotate=args.rotate)
