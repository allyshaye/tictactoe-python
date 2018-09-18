board_dictionary = board_dictionary(board)

current_tile = 'x'
opponent_tile = 'o'

game_over = False

while not game_over:
  make_move(current_tile, opponent_tile, board_dictionary, board)
          
  print("--------------") 
  for row in board:
    print(row)
  results = check_board(board_dictionary, current_tile) 
  if results[3] or full_board(board): 
    print "Game Over! Winner = %s Loser = %s" %(current_tile, opponent_tile)
    game_over = True  

  placeholder = current_tile
  current_tile = opponent_tile
  opponent_tile = placeholder
