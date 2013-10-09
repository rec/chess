from __future__ import absolute_import, division, print_function, unicode_literals

import copy

STARTING_BOARD_DESC = [
  'rnbqkbnr',
  'pppppppp',
  '        ',
  '        ',
  '        ',
  '        ',
  '        ',
  '        ',
  'PPPPPPPP',
  'RNBQKBNR'
  ]

BLACK = False
WHITE = True
EMPTY = ' '

STARTING_BOARD = [[p for p in row] for row in STARTING_BOARD_DESC]

class Game(object):
  def __init__(self):
    self.board = copy.deepcopy(STARTING_BOARD)
    self.last_pawn_move_or_capture = -1
    self.castle_possible = [True, True]
    self.board_history = []
    self.last_pawn_move_two = None  # en passant
    self.captured = ''

  def move_number(self):
    return len(self.board_history)

  def apply_move(self, begin, end):
    self.board_history.append(self.board)
    self.board = copy.deepcopy(self.board)
    bx, by = begin
    ex, ey = end

    begin_piece = self.board[by][bx]
    assert begin_piece is not EMPTY

    side_to_move = BLACK if self.move_number() % 2 else WHITE
    if side_to_move is BLACK:
      assert begin_piece.islower()
    else:
      assert begin_piece.isupper()

    self.board[by][bx] = EMPTY
    end_piece = self.board[ey][ex]
    self.board[ey][ex] = begin_piece
    if end_piece != EMPTY:
      self.captured += end_piece
      self.last_pawn_move_or_capture = self.move_number()

    if begin_piece in 'pP':
      self.last_pawn_move_or_capture = self.move_number()

    if begin_piece == 'k':
      self.castle_possible[BLACK] = False

    if begin_piece == 'K':
      self.castle_possible[WHITE] = False

  def has_piece_between(self, begin, end):
    bx, by = begin
    ex, ey = end
    dx = ex - bx
    dy = ey - by

    if abs(dx) == 1 and abs(dy) == 2:
      return False
    if abs(dx) == 2 and abs(dy) == 1:
      return False

    assert abs(dx) == abs(dy) or not dy or not dy
    delta = max(abs(dx), abs(dy))
    ddx = dx / delta
    ddy = dy / delta

    for d in range(1, delta):
      x = bx + ddx * d
      y = by + ddy * d
      if self.board[by][bx] != EMPTY:
        return False
    return True

  def print_board(self):
    for row in self.board:
      print(''.join(row))


def algebraic_to_coords(alg):
  col, row = alg.lower()
  x = ord(col) - ord('a')
  y = 7 - (ord(row) - ord('1'))
  return x, y
