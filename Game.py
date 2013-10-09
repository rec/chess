from __future__ import absolute_import, division, print_function, unicode_literals

import copy

import Board
import Pieces

from Constants import *

def is_black(piece):
  return piece.islower()

class Game(object):
  def __init__(self, board=None):
    self.board = Board.Board(board)
    self.last_pawn_move_or_capture = -1
    self.castle_possible = [True, True]
    self.board_history = []
    self.last_pawn_move_two = None  # en passant
    self.captured = ''
    self.side_to_move = WHITE

  def move_number(self):
    return len(self.board_history)

  def apply_move(self, begin, end):
    self.board_history.append(self.board)
    self.board = copy.deepcopy(self.board)
    bx, by = begin
    ex, ey = end
    dx = ex - bx
    dy = ey - by

    begin_piece = self.board.get(bx, by)
    assert begin_piece != EMPTY

    if self.side_to_move == BLACK:
      assert is_black(begin_piece), begin_piece
    else:
      assert not is_black(begin_piece), begin_piece

    self.board.set(bx, by, EMPTY)
    end_piece = self.board.get(ex, ey)
    self.board.set(ex, ey, begin_piece)

    if begin_piece in 'pP':
      self.last_pawn_move_or_capture = self.move_number()
      if abs(dy) == 2:
        self.last_pawn_move_two = bx
      else:
        self.last_pawn_move_two = None
      if end_piece == EMPTY and abs(dx):
        assert self.last_move_pawn_two == bx
        end_piece = self.board.get(bx, ey)
        assert end_piece in 'pP'
        self.board.set(bx, ey, EMPTY)
        self.last_pawn_move_two = None
    else:
      self.last_pawn_move_two = None

    if end_piece != EMPTY:
      self.captured += piece
      self.last_pawn_move_or_capture = self.move_number()

    if begin_piece in 'kK':
      if abs(dx) > 1:
        assert self.castle_possible[self.side_to_move]
        if dx > 0:
          rx = 7
          drx = -2
        else:
          rx = 0
          drx = 2
        rook = self.board.get(rx, by)
        assert rook in 'rR'
        self.board.set(rx, by, EMPTY)
        assert self.board.get(rx, by + drx) == EMPTY
        self.board.set(rx, by + drx, rook)

      self.castle_possible[self.side_to_move] = False
    self.side_to_move = not self.side_to_move

  def get_legal_moves(self, begin):
    pass

def algebraic_to_coords(alg):
  col, row = alg.lower()
  x = ord(col) - ord('a')
  y = 7 - (ord(row) - ord('1'))
  assert 0 <= x <= 7
  assert 0 <= y <= 7
  return x, y
