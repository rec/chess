from __future__ import absolute_import, division, print_function, unicode_literals

PIECES = 'rnbqkrp'
INITIAL_DESC = 'rnbqkbnr/pppppppp/////PPPPPPPP/RNBQKBNR'

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

def to_board(desc=None):
  desc = desc or INITIAL_DESC
  board = [to_row(row) for row in desc.split('/')]
  while len(board) < 8:
    board.append('        ')
  return board


