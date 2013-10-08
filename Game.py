from __future__ import absolute_import, division, print_function, unicode_literals

import copy

STARTING_BOARD = [
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

class Chess(object):
  def __init__(self):
    self.board = copy.deepcopy(STARTING_BOARD)
    self.move_count = 0
    self.last_pawn_move_or_capture = -1
    self.castle_possible = [True, True]
    self.board_history = []
    self.last_pawn_move = None

