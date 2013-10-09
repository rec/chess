#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals

import sys

import Game
import Pieces

def chess():
  game = Game.Game(len(sys.argv) > 1 and sys.argv[1])
  while True:
    game.board.print_board()
    move = raw_input('Enter a move looking like a1-a3: ').strip().lower()
    if not move:
      continue
    if 'quit'.startswith(move):
      break
    moves = [Game.algebraic_to_coords(m) for m in move.split('-')]
    assert not game.board.has_piece_between(*moves), "There was a piece in the way"
    game.apply_move(*moves)

  print('Goodbye')


if __name__ == '__main__':
  chess()
