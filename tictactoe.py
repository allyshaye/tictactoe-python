import random


def create_board():
  board = [
    ['x', 'x', 'o'],
    ['x', 'o', '-'],
    ['o', '-', '-']
  ]
  return board

# GOAL IS TO GET RID OF BOARD_DICT AND JUST USE ROW_TO_BOX_DEFS BISHH
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


def row_to_box_defs():
  box_dict = {
    'top_row': [[0,0], [0,1], [0,2]],
    'mid_row': [[1,0], [1,1], [1,2]],
    'bottom_row': [[2,0], [2,1], [2,2]],
    'left_col': [[0,0], [1,0], [2,0]],
    'mid_col': [[0,1], [1,1], [2,1]],
    'right_col': [[0,2], [1,2], [2,2]],
    'diag_top_left_down': [[0,0], [1,1], [2,2]],
    'diag_bot_left_up': [[2,0], [1,1], [0,2]]
  }

  return box_dict


def check_board(board_dict, tile):
  results = { 3: [], 2: [], 1: [], 0: [] }

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


def move_on_twos_row_choice(board_dict, row_list):
  next_move = ''
  for row in row_list:
    row_contents = board_dict[row]
    if '-' in row_contents:
      next_move = row
      break
  return next_move


def random_row_choice(row_list):
  next_move = random.choice(row_list)
  return next_move


def determine_next_row(board_dict, self_results, opponent_results):
  row_found = False
  next_row = ''

  if self_results[2]: # win game
    next_row = move_on_twos_row_choice(board_dict, self_results[2])
    available_spots = 1
    if next_row != '': row_found = True

  if opponent_results[2] and not row_found: # prevent opponent from winning
    next_row = move_on_twos_row_choice(board_dict, opponent_results[2])
    available_spots = 1
    if next_row != '': row_found = True

  if not row_found: # make 2 in a row
    if self_results[1]:
      for row in self_results[1]:
        row_contents = board_dict[row]
        if row_contents.count('-') == 2:
          row_found = True
          next_row = row
          available_spots = 2
          break

  if not row_found: # play first move
    avail_rows = self_results[1] + self_results[0]
    next_row = random_row_choice(self_results[0])
    available_spots = 3

  return [next_row, available_spots]


def determine_next_box(row_box_dict, board, row_data, tile):
  row_boxes = row_box_dict[row_data[0]]
  available_spots = row_data[1] 

  if available_spots == 1: 
    for box in row_boxes:
      if board[box[0]][box[1]] == '-':
        next_box = box
  
  if available_spots == 2:
    avail_spots = []
    for box in row_boxes: #indices
      if board[box[0]][box[1]] == '-':
        avail_spots.append(box)
    next_box = random.choice(avail_spots)

  if available_spots == 3:
    next_box = random.choice(row_boxes)

  print(next_box)
  return next_box




