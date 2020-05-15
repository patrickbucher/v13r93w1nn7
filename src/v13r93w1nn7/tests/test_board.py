import pytest

import board


def test_create_empty_board():
    b = board.Board()
    assert b.rows() == board.ROWS
    assert b.cols() == board.COLS


@pytest.mark.parametrize('l', [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 1, 1, 2, 0, 0],
    ],
    [
        [0, 1, 2, 0, 1, 2, 0],
        [0, 1, 2, 0, 1, 2, 0],
        [0, 1, 2, 0, 1, 2, 0],
        [0, 1, 2, 0, 1, 2, 0],
        [0, 1, 2, 0, 1, 2, 0],
        [0, 1, 2, 0, 1, 2, 0],
    ],
])
def test_from_list(l):
    board.Board.from_list(l)


@pytest.mark.parametrize('l', [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0],  # error: 4
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 1, 2, 1, 0],
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 0, 0, 0],  # error: 3
    ],
])
def test_from_list_fail(l):
    with pytest.raises(ValueError) as err:
        board.Board.from_list(l)
    assert 'only values [0, 1, 2] allowed' in str(err.value)


@pytest.mark.parametrize('l,valid_moves', [
    ([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ], [0, 1, 2, 3, 4, 5, 6]),
    ([
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 2, 2, 0, 0],
        [0, 0, 1, 2, 1, 0, 0],
        [0, 1, 2, 1, 1, 2, 0],
    ], [0, 1, 2, 3, 5, 6]),
    ([
        [0, 2, 0, 0, 1, 0, 0],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 1, 1, 1, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 2, 1, 1, 2],
        [1, 1, 2, 1, 1, 2, 1],
    ], [0, 2, 3, 5, 6]),
    ([
        [2, 2, 0, 1, 1, 0, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 1, 1, 1, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 2, 1, 1, 2],
        [1, 1, 2, 1, 1, 2, 1],
    ], [2, 5]),
    ([
        [2, 2, 1, 1, 1, 0, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 1, 1, 1, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 2, 1, 1, 2],
        [1, 1, 2, 1, 1, 2, 1],
    ], [5]),
    ([
        [2, 2, 1, 1, 1, 1, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 1, 1, 1, 2],
        [1, 1, 2, 2, 2, 2, 1],
        [2, 2, 1, 2, 1, 1, 2],
        [1, 1, 2, 1, 1, 2, 1],
    ], []),
])
def test_valid_moves(l, valid_moves):
    b = board.Board.from_list(l)
    moves = b.valid_moves()
    assert moves == valid_moves


@pytest.mark.parametrize('before,player,move,after', [
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        1, 3,
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
        2, 3,
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 2, 1, 1, 0, 0, 0],
        ],
        2, 2,
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 2, 1, 1, 0, 0, 0],
        ],
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 2, 1, 1, 0, 0, 0],
        ],
        1, 6,
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 2, 1, 1, 0, 0, 1],
        ],
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ],
        2, 3,
        [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ],
    ),
])
def test_apply_move(before, player, move, after):
    b = board.Board.from_list(before)
    b = b.apply_move(player, move)
    assert b.as_list() == after


@pytest.mark.parametrize('before,player,move', [
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        1, 8,
    ),
    (
        [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ],
        1, 3,
    ),
    (
        [
            [2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1],
        ],
        2, 2,
    ),
])
def test_apply_invalid_move(before, player, move):
    b = board.Board.from_list(before)
    with pytest.raises(ValueError) as err:
        b.apply_move(player, move)
    assert f'{move} is not a valid move' in str(err.value)


@pytest.mark.parametrize('l,expected', [
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        {
            1: [],
            2: [],
        },
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
            [0, 0, 2, 1, 0, 0, 0],
        ],
        {
            1: [[(2, 3), (3, 3), (4, 3), (5, 3)]],
            2: [],
        },
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0],
            [2, 0, 2, 1, 0, 0, 0],
            [2, 0, 2, 1, 0, 0, 0],
            [2, 0, 2, 1, 0, 0, 0],
            [1, 0, 2, 1, 1, 1, 1],
        ],
        {
            1: [
                [(2, 3), (3, 3), (4, 3), (5, 3)],
                [(5, 3), (5, 4), (5, 5), (5, 6)],
            ],
            2: [
                [(1, 0), (2, 0), (3, 0), (4, 0)],
                [(2, 2), (3, 2), (4, 2), (5, 2)],
            ],
        },
    ),
    (
        [
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
        ],
        {
            1: sorted([
                [(0, 1), (1, 2), (2, 3), (3, 4)],
                [(0, 3), (1, 4), (2, 5), (3, 6)],
                [(0, 3), (1, 2), (2, 1), (3, 0)],
                [(0, 5), (1, 4), (2, 3), (3, 2)],
                [(1, 0), (2, 1), (3, 2), (4, 3)],
                [(1, 2), (2, 3), (3, 4), (4, 5)],
                [(1, 4), (2, 3), (3, 2), (4, 1)],
                [(1, 6), (2, 5), (3, 4), (4, 3)],
                [(2, 1), (3, 2), (4, 3), (5, 4)],
                [(2, 3), (3, 4), (4, 5), (5, 6)],
                [(2, 3), (3, 2), (4, 1), (5, 0)],
                [(2, 5), (3, 4), (4, 3), (5, 2)],
            ]),
            2: sorted([
                [(0, 0), (1, 1), (2, 2), (3, 3)],
                [(0, 2), (1, 3), (2, 4), (3, 5)],
                [(0, 4), (1, 3), (2, 2), (3, 1)],
                [(0, 6), (1, 5), (2, 4), (3, 3)],
                [(1, 1), (2, 2), (3, 3), (4, 4)],
                [(1, 3), (2, 4), (3, 5), (4, 6)],
                [(1, 3), (2, 2), (3, 1), (4, 0)],
                [(1, 5), (2, 4), (3, 3), (4, 2)],
                [(2, 0), (3, 1), (4, 2), (5, 3)],
                [(2, 2), (3, 3), (4, 4), (5, 5)],
                [(2, 4), (3, 3), (4, 2), (5, 1)],
                [(2, 6), (3, 5), (4, 4), (5, 3)],
            ]),
        },
    ),
])
def test_wins(l, expected):
    b = board.Board.from_list(l)
    expected == b.wins()
