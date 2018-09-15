from tictactoe import *

board = create_board()


board_dictionary = row_definitions(board)

results_o = check_board(board_dictionary, 'o')
results_x = check_board(board_dictionary, 'x')

# for i,j in results_x.items():
#   print "%s ===== %s" %(i,j)

# print(results_o)
# print(results_x)
# print(game_over(results_o))
# print(game_over(results_x))
next_row_data = determine_next_row(board_dictionary, results_x, results_o)
# print(next_row)
row_to_box_dict = row_to_box_defs()
determine_next_box(row_to_box_dict, board, next_row_data, 'o')


