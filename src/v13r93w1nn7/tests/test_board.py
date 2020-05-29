import pytest

import board


def test_create_empty_board():
    b = board.Board()
    assert b.rows() == board.ROWS
    assert b.cols() == board.COLS


@pytest.mark.parametrize('lst', [
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
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 3, 0, 0, 0, 0],
        [3, 2, 1, 3, 2, 2, 1],
    ],
])
def test_from_list(lst):
    board.Board.from_list(lst)


@pytest.mark.parametrize('lst', [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0],  # error: 4
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [3, 1, 2, 1, 2, 1, 0],
    ],
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [3, 1, 2, 4, 3, 0, 0],  # error: 4
    ],
])
def test_from_list_fail(lst):
    with pytest.raises(ValueError) as err:
        board.Board.from_list(lst)
    assert 'only values [0, 1, 2, 3] allowed' in str(err.value)


@pytest.mark.parametrize('lst,valid_moves', [
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
    ([
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0],
        [0, 0, 3, 2, 0, 0, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [0, 3, 2, 1, 1, 3, 0],
    ], [0, 1, 3, 4, 5, 6]),
])
def test_valid_moves(lst, valid_moves):
    b = board.Board.from_list(lst)
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
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ],
        3, 0,
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0],
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
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 1, 2, 1, 2],
        ],
        3, 3,
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


@pytest.mark.parametrize('lst,expected', [
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ], False
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
        ], False
    ),
    (
        [
            [1, 2, 1, 0, 1, 2, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
        ], False
    ),
    (
        [
            [1, 2, 1, 2, 1, 2, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
        ], True
    ),
    (
        [
            [0, 3, 0, 3, 0, 3, 0],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 3, 1],
            [1, 2, 1, 2, 3, 2, 1],
            [1, 2, 3, 3, 1, 2, 1],
            [3, 3, 2, 1, 2, 1, 2],
        ], False
    ),
    (
        [
            [1, 3, 3, 3, 1, 3, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 3, 1],
            [1, 2, 1, 2, 3, 2, 1],
            [1, 2, 3, 3, 1, 2, 1],
            [3, 3, 2, 1, 2, 1, 2],
        ], True
    ),
])
def test_is_draw(lst, expected):
    b = board.Board.from_list(lst)
    assert b.is_draw() == expected


@pytest.mark.parametrize('lst,expected', [
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
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 0, 0, 0, 0],
            [2, 1, 0, 0, 0, 0, 0],
            [1, 2, 0, 3, 3, 3, 3],
        ],
        {
            1: [],
            2: [],
        },
    ),
])
def test_wins(lst, expected):
    b = board.Board.from_list(lst)
    expected == b.wins()


@pytest.mark.parametrize('lst,indent,p1,p2,pn,empty,slotnums,expected', [
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 2, 0, 0, 0],
            [0, 1, 2, 1, 1, 2, 0],
        ], ' ', 'x', 'o', '/', '_', True,
        ' 1 2 3 4 5 6 7\n' +
        ' _ _ _ _ _ _ _\n' +
        ' _ _ _ _ _ _ _\n' +
        ' _ _ _ _ _ _ _\n' +
        ' _ x _ _ _ _ _\n' +
        ' _ o x o _ _ _\n' +
        ' _ x o x x o _\n'
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 3, 0, 2, 0, 0],
            [0, 0, 1, 1, 2, 0, 0],
            [3, 0, 1, 3, 2, 2, 3],
        ], ' ', 'x', 'o', '/', '_', True,
        ' 1 2 3 4 5 6 7\n' +
        ' _ _ _ _ _ _ _\n' +
        ' _ _ _ _ _ _ _\n' +
        ' _ _ _ _ x _ _\n' +
        ' _ _ / _ o _ _\n' +
        ' _ _ x x o _ _\n' +
        ' / _ x / o o /\n'
    ),
    (
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 2, 3, 0, 0],
            [0, 1, 2, 1, 1, 2, 0],
        ], '\t', '#', '@', '*', '-', False,
        '\t- - - - - - -\n' +
        '\t- - - - - - -\n' +
        '\t- - - - - - -\n' +
        '\t- # - - - - -\n' +
        '\t- @ # @ * - -\n' +
        '\t- # @ # # @ -\n'
    ),
])
def test_draw(lst, indent, p1, p2, pn, empty, slotnums, expected):
    b = board.Board.from_list(lst)
    assert expected == b.draw(
        indent=indent,
        p1=p1,
        p2=p2,
        pn=pn,
        empty=empty,
        slotnums=slotnums)
