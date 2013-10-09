#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals

import Game
import Pieces

def chess():
  game = Game.Game()
  while True:
    game.print_board()
    move = raw_input('Enter a move looking like a1-a3: ').strip()
    moves = [Game.algebraic_to_coords(m) for m in move.split('-')]
    assert not game.has_piece_between(*moves), "There was a piece in the way"
    game.apply_move(*moves)

if __name__ == '__main__':
  chess()
