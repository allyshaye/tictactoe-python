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
    ['x', 'o', '-'],
    ['-', 'o', '-']
  ]
  return board


def top_row(board):
  return board[0]

def mid_row(board):
  return board[1]

def bottom_row(board):
  return board[2]

def left_col(board):
  left_col = [board[0][0], board[1][0], board[2][0]]
  return left_col

def mid_col(board):
  mid_col = [board[0][1], board[1][1], board[2][1]]
  return mid_col

def right_col(board):
  right_col = [board[0][2], board[1][2], board[2][2]]
  return right_col

def diag_top_left_down(board):
  diag = [board[0][0], board[1][1], board[2][2]]
  return diag

def diag_bot_left_up(board):
  diag = [board[2][0], board[1][1], board[0][2]]
  return diag


def audit_board(board, tile):
  board_dict = {
    'top_row': top_row(board),
    'mid_row': mid_row(board),
    'bottom_row': bottom_row(board),
    'left_col': left_col(board),
    'mid_col': mid_col(board),
    'right_col': right_col(board),
    'diag_top_left_down': diag_top_left_down(board),
    'diag_bot_left_up': diag_bot_left_up(board)
  }

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


def game_over(results):
  return True if results[3] else False


# return row to play? given that we checked for game over.
def determine_next_move(self_results, opponent_results):







