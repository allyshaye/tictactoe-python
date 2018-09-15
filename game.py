from tictactoe import *

board = create_board()

board_dictionary = board_dictionary(board)

results_o = check_board(board_dictionary, 'o')
results_x = check_board(board_dictionary, 'x')
next_row_data = determine_next_row(board_dictionary, results_x, results_o)
print(determine_next_box(board_dictionary, board, next_row_data))

