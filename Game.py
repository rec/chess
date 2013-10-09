from __future__ import absolute_import, division, print_function, unicode_literals

import copy

import Board
import Pieces

BLACK = False
WHITE = True
EMPTY = ' '

def is_black(piece):
  return piece.islower()

class Game(object):
  def __init__(self, board=None):
    self.board = board or copy.deepcopy(Board.INITIAL)
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
    dx = ex - bx
    dy = ey - by

    begin_piece = self.board[by][bx]
    assert begin_piece != EMPTY

    side_to_move = WHITE if self.move_number() % 2 else BLACK
    if side_to_move is BLACK:
      assert is_black(begin_piece), begin_piece
    else:
      assert not is_black(begin_piece), begin_piece

    self.board[by][bx] = EMPTY
    end_piece = self.board[ey][ex]
    self.board[ey][ex] = begin_piece

    if begin_piece in 'pP':
      self.last_pawn_move_or_capture = self.move_number()
      if end_piece == EMPTY and abs(dx):
        end_piece = self.board[ey][bx]
        assert end_piece in 'pP'
        self.board[ey][bx] = EMPTY

    if end_piece != EMPTY:
      self.captured += piece
      self.last_pawn_move_or_capture = self.move_number()

    if begin_piece in 'kK':
      if abs(dx) > 1:
        assert self.castle_possible[side_to_move]
        if dx > 0:
          rx = 7
          drx = -2
        else:
          rx = 0
          drx = 2
        rook = self.board[by][rx]
        assert rook in 'rR'
        self.board[by][rx] = EMPTY
        assert self.board[by][rx + drx] == EMPTY
        self.board[by][rx + drx] = rook

      self.castle_possible[side_to_move] = False

  def has_piece_between(self, begin, end):
    bx, by = begin
    ex, ey = end
    dx = ex - bx
    dy = ey - by

    if abs(dx) == 1 and abs(dy) == 2:
      return False
    if abs(dx) == 2 and abs(dy) == 1:
      return False

    assert abs(dx) == abs(dy) or not dx or not dy
    delta = max(abs(dx), abs(dy))
    ddx = dx // delta
    ddy = dy // delta

    for d in range(1, delta):
      x = bx + ddx * d
      y = by + ddy * d
      if self.board[y][x] != EMPTY:
        return True
    return False

  def print_board(self):
    for row in self.board:
      print(''.join(row))


def algebraic_to_coords(alg):
  col, row = alg.lower()
  x = ord(col) - ord('a')
  y = 7 - (ord(row) - ord('1'))
  assert 0 <= x <= 7
  assert 0 <= y <= 7
  return x, y
