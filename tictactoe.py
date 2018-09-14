# we need a board x
# players = 1 human, 1 comp
# human plays an X
# per every play, game logic does the following:
  # determines if there is three in a row?
  # if there isn't 3 in a row, is there 2 in a row?
  # if there is 2 in a row, play it
      # if it's YOUR two in a row, this takes precedence over OPPONENTS.
  # if there isn't 2 in a row, make a move on a row which you are already on!
    # if it's the first play for you, pick a random spot.




def create_board():
  board = [
    ['x', 'o', 'x'],
    ['-', 'o', '-'],
    ['-', 'x', '-']
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
  results = { 3: [], 2: [], 1: [], 0: [] }

  for row_name, row in board_dict.items():
    tile_count = row.count(tile)
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

# needs work
def determine_next_move(board_dict, self_results, opponent_results):
  offense = False
  defense = False
  offensive_move = ''
  defensive_move = ''

  if self_results[2]:
    for row in self_results[2]:
      row_contents = board_dict[row]
      if '-' in row_contents:
        offense = True
        offensive_move = row
        break

  if opponent_results[2]:
    for row in opponent_results[2]:
      print(row)
      row_contents = board_dict[row]
      if '-' in row_contents:
        defense = True
        defensive_move = row
        break

  if not offense and not defense:
    print('we still false yo')

  if offense:
    return offensive_move
  else:
    return defensive_move







