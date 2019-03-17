board = []
def create_board():
	for i in range(3):
		board.append([' ',' ',' '])
def display_board():
	global board
	board_str = ""
	for i in range(3):
		board_str += str(i)
		for j in range(2):
			board_str += board[i][j] + '|'
		board_str += board[i][len(board[i])-1] + '\n'
		if i != 2:
			board_str += ' -----\n'
	board_str+= ' 0 1 2'
	return board_str
def get_move(piece):
	move = int(input("Player " + str(player) +' select a row: '))
	move2 = int(input("Player " + str(player) +' select a column: '))
	try:
		make_move(piece,move,move2)
	except IndexError:
		print("This is not a valid move")
		get_move(piece)

def make_move(piece, index1,index2):
	global board
	if board[index1][index2] != ' ':
		raise IndexError
	board[index1][index2] = piece
def check_win(piece):
	for i in range(len(board)):
		counter = 0
		for j in range(len(board[i])):
			if board[i][j] == piece:
				counter += 1
		if counter == 3:
			return True
	for i in range(len(board)):
		counter = 0
		for j in range(len(board[i])):
			if board[j][i] == piece:
				counter += 1
			if counter == 3:
				return True
	if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece:
		return True
	if board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
		return True
	return False
if __name__ == '__main__':
	create_board()
	player = 1
	piece = 'O'
	while(True):
		print(display_board())
		get_move(piece)
		if(check_win(piece) == True):
			break
		if piece == 'O':
			piece = 'X'
		else:
			piece = 'O'
		if player == 1:
			player = 2
		else:
			player = 1
	print(display_board())
	print("Player " + str(player) + ' Wins')

