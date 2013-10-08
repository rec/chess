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

