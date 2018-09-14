from tictactoe import *

board = create_board()


# for row in board:
  # print(row)

board_dictionary = row_definitions(board)
# print(board_dict['left_col'])
# for i,j in board_dict.items():
#   print "%s ---- %s" %(i, j)
results_o = audit_board(board_dictionary, 'o')
results_x = audit_board(board_dictionary, 'x')

# for i,j in results_x.items():
#   print "%s ===== %s" %(i,j)

# print(results_o)
# print(results_x)
# print(game_over(results_o))
# print(game_over(results_x))
nextt = determine_next_move(board_dictionary, results_o, results_x)
print(nextt)


  # board = [
  #   ['x', 'o', 'x'],
  #   ['x', 'o', '-'],
  #   ['-', 'x', 'x']
  # ]

