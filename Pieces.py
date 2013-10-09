from __future__ import absolute_import, division, print_function, unicode_literals

WHITE_PAWN_MOVE = [
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
]

WHITE_PAWN_CAPTURE = [
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1,  0,  1, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
]

BLACK_PAWN_MOVE = [
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
]

BLACK_PAWN_CAPTURE = [
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 1,  0,  1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
]

ROOK = [
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],

  [1, 1, 1, 1, 1, 1, 1,  0,  1, 1, 1, 1, 1, 1, 1],

  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 0],
]

QUEEN = [
  [1, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0, 0,  1,  0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0,  1,  0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0,  1,  0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0,  1,  0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1,  1,  1, 0, 0, 0, 0, 0, 0],

  [1, 1, 1, 1, 1, 1, 1,  0,  1, 1, 1, 1, 1, 1, 1],

  [0, 0, 0, 0, 0, 0, 1,  1,  1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0,  1,  0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0,  1,  0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0,  1,  0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0,  1,  0, 0, 0, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0,  1,  0, 0, 0, 0, 0, 0, 1],
]

BISHOP = [
  [1, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0, 0,  0,  0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0,  0,  0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0,  0,  0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0,  0,  0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1,  0,  1, 0, 0, 0, 0, 0, 0],

  [1, 1, 1, 1, 1, 1, 1,  0,  1, 1, 1, 1, 1, 1, 1],

  [0, 0, 0, 0, 0, 0, 1,  0,  1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0,  0,  0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0,  0,  0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0,  0,  0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0,  0,  0, 0, 0, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 1],
]

KNIGHT = [
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1,  0,  1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0,  0,  0, 1, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 1, 0,  0,  0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1,  0,  1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
]

KING = [
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1,  1,  1, 0, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 1, 1,  0,  1, 1, 0, 0, 0, 0, 0],

  [0, 0, 0, 0, 0, 0, 1,  1,  1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0,  0,  0, 0, 0, 0, 0, 0, 0],
]

MOVES = {
  'P': WHITE_PAWN_MOVE,
  'p': BLACK_PAWN_MOVE,
  'N': KNIGHT,
  'K': KING,
  'Q': QUEEN,
  'R': ROOK,
  'B': BISHOP,
  'n': KNIGHT,
  'k': KING,
  'q': QUEEN,
  'r': ROOK,
  'b': BISHOP,
  }

BOARD_OFFSET = 7

def allowed_move(begin, end, piece):
  x = end[0] - begin[0] + BOARD_OFFSET
  y = end[1] - begin[1] + BOARD_OFFSET
  return piece[y][x]

def piece_move(begin, piece):
  """List of coords we could move to if there were no other pieces on the
  board."""

  for y in range(8):
    for x in range(8):
      end = x, y
      if allowed_move(begin, end, piece):
        yield end

def moves_on_board(moves):
  board = [[0] * 8 for i in range(8)]

  for x, y in moves:
    board[y][x] = 1

  for row in board:
    for entry in row:
      print('X' if entry else '.', end='')
    print()

def board_piece_moves(begin, piece):
  moves_on_board(piece_move(begin, piece))
