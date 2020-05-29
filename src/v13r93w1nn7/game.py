#!/usr/bin/env python3

import argparse
import random
import os

from board import Board


def main(neutral=False):
    b = Board()
    p1, p2, pn = (1, 'x', 'X'), (2, 'o', 'O'), (3, '.', '.')
    lower, upper = 1, b.cols()
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
        clear()
        print(draw(b))
        played = False
        while not played:
            entered = input(f'Player {p[0]} [{p[1]}] ({lower} to {upper}): ')
            try:
                slot = int(entered)
                if lower <= slot <= upper and (slot-1) in b.valid_moves():
                    b = b.apply_move(p[0], slot-1)
                    played = True
                else:
                    wrong_move(lower, upper)
            except ValueError:
                wrong_move(lower, upper)
        wins = b.wins()
        if wins[p[0]]:
            clear()
            coords = wins[p[0]][0]
            winner_board = highlight_winner(b, draw, coords, p[2])
            print(winner_board)
            print(f'Player {p[0]} has won the game.')
            finished = True
        elif b.is_draw():
            clear()
            print(draw(b))
            print('The game ended in a draw.')
            finished = True
        p = p2 if p == p1 else p1


def highlight_winner(b, draw, coords, new):
    winner_board = b.as_list()
    for f in coords:
        winner_board[f[0]][f[1]] = 9  # dummy value
    new_b = Board.from_list(winner_board, validate=False)
    output = draw(new_b)
    return output.replace('?', new)


def wrong_move(lower, upper):
    print(f'You must pick a free slot between {lower} and {upper}!')


def decorate_draw(p1, p2, pn, empty, slotnums):
    def _draw(b):
        return b.draw(p1=p1, p2=p2, pn=pn, empty=empty, slotnums=slotnums)
    return _draw


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='v13r93w1nn7')
    parser.add_argument(
        '--neutral', default=False, action='store_true',
        help='enable neutral stones falling randomly before every round')
    args = parser.parse_args()
    print(args.neutral)
    main(neutral=args.neutral)
