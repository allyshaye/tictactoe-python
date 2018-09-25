from tictactoe import *

board = create_board()
bd = board_dictionary(board)

current_tile = 'x'
opponent_tile = 'o'

game_over = False

while not game_over:
  board = make_move(current_tile, opponent_tile, bd, board)
  bd = board_dictionary(board)

  print_board(board)  
  
  results = check_board(bd, current_tile)

  if full_board(board) or results[3]:
    game_over = True
    print("Game over!")

    if results[3]:
      print "Winner = %s, Loser = %s" %(current_tile, opponent_tile)
    else:
      print("It's a tie!")

  placeholder = current_tile
  current_tile = opponent_tile
  opponent_tile = placeholder
