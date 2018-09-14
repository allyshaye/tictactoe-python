from tictactoe import *

board = create_board()


# for row in board:
  # print(row)


results_o = audit_board(board, 'o')
results_x = audit_board(board, 'x')

print(game_over(results_o))
print(game_over(results_x))
