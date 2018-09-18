import random


def create_board():
  board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
  ]
  return board


def board_dictionary(board):
  board_dict = {
    'top_row': [[[0,0], [0,1], [0,2]], board[0]],
    'mid_row': [[[1,0], [1,1], [1,2]], board[1]],
    'bottom_row': [[[2,0], [2,1], [2,2]], board[2]],
    'left_col': [[[0,0], [1,0], [2,0]], [board[0][0], board[1][0], board[2][0]]],
    'mid_col': [[[0,1], [1,1], [2,1]], [board[0][1], board[1][1], board[2][1]]],
    'right_col': [[[0,2], [1,2], [2,2]], [board[0][2], board[1][2], board[2][2]]],
    'diag_top_left_down': [[[0,0], [1,1], [2,2]],[board[0][0], board[1][1], board[2][2]]],
    'diag_bot_left_up': [[[2,0], [1,1], [0,2]],[board[2][0], board[1][1], board[0][2]]]
  }

  return board_dict


def check_board(board_dict, tile):
  results = { 3: [], 2: [], 1: [], 0: [] }

  for row_name, row_contents in board_dict.items():
    tile_count = row_contents[1].count(tile)
    if tile_count == 3:
      results[3].append(row_name)
    elif tile_count == 2:
      results[2].append(row_name)
    elif tile_count == 1:
      results [1].append(row_name)
    elif tile_count == 0:
      results[0].append(row_name)
  return results


def full_board(board):
  full = True
  for row in board:
    if '-' in row:

