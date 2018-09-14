import random


def create_board():
  board = [
    ['o', 'x', '-'],
    ['-', 'x', '-'],
    ['-', '-', '-']
  ]
  return board


def row_definitions(board):
  board_dict = {
    'top_row': board[0],
    'mid_row': board[1],
    'bottom_row': board[2],
    'left_col': [board[0][0], board[1][0], board[2][0]],
    'mid_col': [board[0][1], board[1][1], board[2][1]],
    'right_col': [board[0][2], board[1][2], board[2][2]],
    'diag_top_left_down': [board[0][0], board[1][1], board[2][2]],
    'diag_bot_left_up': [board[2][0], board[1][1], board[0][2]]
  }
  return board_dict


def audit_board(board_dict, tile):
  results = { 
    3: [], 
    2: [], 
    1: [], 
    0: [] 
  }

  for row_name, row_contents in board_dict.items():
    tile_count = row_contents.count(tile)
    if tile_count == 3:
      results[3].append(row_name)
    elif tile_count == 2:
      results[2].append(row_name)
    elif tile_count == 1:
      results [1].append(row_name)
    elif tile_count == 0:
      results[0].append(row_name)

  return results


def game_over(results_dict):
  return True if results_dict[3] else False

# return row
def move_on_twos(board_dict, row_list):
  next_move = ''
  for row in row_list:
    row_contents = board_dict[row]
    if '-' in row_contents:
      next_move = row
      break
  return next_move

def first_move(row_list):
  return next_move = random.choice(row_list)


# needs refactoring; returns ROW to play
def determine_next_row(board_dict, self_results, opponent_results):
  move_found = False
  next_move = ''

  if self_results[2]:
    next_move = move_on_twos(board_dict, self_results[2])
    if next_move != '':
      move_found = True

  if opponent_results[2] and not move_found:
    next_move = move_on_twos(board_dict, opponent_results[2])
    if next_move != '':
      move_found = True

  if not move_found:
    if self_results[1]:
      for row in self_results[1]:
        if row.count('-') == 2:
          move_found = True
          next_move = row
          break

  if not move_found:
    if self_results[0]:
      next_move = first_move(self_results[0])
      if next_move != '':
        move_found = True # don't think i need this since it's the last check.

  return next_move


def determine_next_spot(board_dict, move):
  pass




