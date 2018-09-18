Last login: Tue Sep 18 14:19:36 on ttys000
megamouth:~ aines$ cd Desktop/
megamouth:Desktop aines$ ls
Screen Shot 2018-07-30 at 1.52.06 PM.png
Screen Shot 2018-08-01 at 12.35.34 PM.png
Screen Shot 2018-08-01 at 12.36.14 PM.png
Screen Shot 2018-08-01 at 9.41.55 AM.png
Screen Shot 2018-08-08 at 12.24.33 PM.png
Screen Shot 2018-08-08 at 12.25.13 PM.png
Screen Shot 2018-08-08 at 3.25.20 PM.png
Screen Shot 2018-08-08 at 3.25.22 PM.png
Total Workforce Management (TWM) - Annual Security Refresher.pdf
Total Workforce Management (TWM) - Suicide Awareness Training.pdf
Total Workforce Management (TWM) Active Shooter.pdf
notes.rtf
python_scripting
tictactoe-python-master
to_do_08082018.rtf
megamouth:Desktop aines$ cd tictactoe-python-master/
megamouth:tictactoe-python-master aines$ ls
README.md	game.py		tictactoe.py
megamouth:tictactoe-python-master aines$ vim tictactoe.py 


      for row in self_results[1]:
        row_contents = board_dict[row][1]
        if row_contents.count('-') == 2:
          row_found = True
          next_row = row
          available_spots = 2
          break

  if not row_found:
    if self_results[0]:
      next_row = random_row_choice(self_results[0])
      available_spots = 3

  return [next_row, available_spots]


def determine_next_box(board_dict, board, row_data):
  row_boxes = board_dict[row_data[0]][0]
  available_spots = row_data[1]

  if available_spots == 1:
    for box in row_boxes:
      if board[box[0]][box[1]] == '-':
        next_box = box

  if available_spots == 2:
    avail_spots = []
    for box in row_boxes:
      if board[box[0]][box[1]] == '-':
        avail_spots.append(box)
    next_box = random.choice(avail_spots)

  if available_spots == 3:
    next_box = random.choice(row_boxes)

  return next_box



def make_move(self_tile, opponent_tile, board_dict, board):
  opponent_results = check_board(board_dict, opponent_tile)
  self_results = check_board(board_dict, self_tile)
  next_row = determine_next_row(board_dict, self_results, opponent_results)
  next_spot = determine_next_box(board_dict, board, next_row)
  board[next_spot[0]][next_spot[1]] = self_tile
