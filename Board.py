from __future__ import absolute_import, division, print_function, unicode_literals

from Constants import *

def to_row(row):
  result = []
  for r in row:
    if r in '12345678':
      result +=  [' '] * int(r)
    else:
      assert r.lower() in PIECES, r
      result.append(r)

  while len(result) < 8:
    result += ' '
  return result


class Board(object):
  def __init__(self, desc=None):
    desc = desc or INITIAL_DESC
    self.board = [to_row(row) for row in desc.split('/')]
    while len(self.board) < 8:
      self.board.append('        ')

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

  def get(self, x, y):
    return self.board[y][x]

  def set(self, x, y, piece):
    self.board[y][x] = piece

  def print_board(self):
    for row in self.board:
      print(''.join(row))

