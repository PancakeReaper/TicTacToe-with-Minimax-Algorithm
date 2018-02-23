
def printScoreBoard(botPlayer=False):
	print("+---------------------+")
	print("   Player 1 wins: " + str(playerOneWins))
	if botPlayer:
		print("  Minimax Bot wins: " + str(playerTwoWins))
	else:
		print("   Player 2 wins: " + str(playerTwoWins))
	print("     " + str(tieGames) + " tie game(s)")
	print("+---------------------+")

def isPlayPossible():
	for r in board:
		for c in r:
			if c == " ":
				return True
	return False

def isGameOver():
	mid = board[1][1]
	if mid != " ":
		if board[0][0] == mid and board[2][2] == mid:
			return True
		elif board[0][2] == mid and board[2][0] == mid:
			return True
	for r in range(3):
		if board[r][0] == board[r][1] and board[r][1] == board[r][2]:
			if board[r][0] != " ":
				return True
		if board[0][r] == board[1][r] and board[1][r] == board[2][r]:
			if board[0][r] != " ":
				return True
	return False

def boardToString():
	print(" | 1 | 2 | 3 | ")
	for r in range(3):
		print("-+---+---+---+-")
		row = str(r+1) + "| "
		for c in board[r]:
			row += c + " | " 
		print(row)
	print("")

def makeMove(player):
	if player == 1:
		mark = "X"
	else:
		mark = "O"
	notMadeMove = True
	while notMadeMove:
		move = input("Make your move Player " + str(player) + " using coordinates. ")
		try:
			movex = int(move[0]) - 1
			movey = int(move[2]) - 1
		except:
			print("Please input coordinates in the following format: x, y")
			movex = -1
			movey = -1
		if movex != -1 and board[movey][movex] == " ":
			board[movey][movex] = mark
			notMadeMove = False
		elif movex != -1:
			print("You have selected an invalid location to play")

def startGame():
	boardToString()
	while not isGameOver():
		makeMove(1)
		boardToString()
		if isGameOver():
			print("Player 1 wins!!")
			return 1
		elif not isPlayPossible():
			print("Tie game!!")
			return 0

		makeMove(2)
		boardToString()
		if isGameOver():
			print("Player 2 wins!!")
			return 2
		elif not isPlayPossible():
			print("Tie Game!!")
			return 0

def clearBoard():
	for r in range(3):
		for c in range(3):
			board[r][c] = " "

def askForAnotherGame():
	for r in board:
		for c in r:
			c = " "
	ans = input("Would you like to play another game? ")
	print()
	if ans.lower() == "y" or ans.lower() == "yes":
		clearBoard()
		return True
	return False

board = []
for r in range(3):
	board_row = []
	for c in range(3):
		board_row.append(" ")
	board.append(board_row)

playerOneWins = 0
playerTwoWins = 0
tieGames = 0

if __name__ == "__main__":
	stillPlaying = True
	while stillPlaying:
		winner = startGame()
		if winner == 2:
			playerTwoWins += 1
		elif winner == 1:
			playerOneWins += 1
		else:
			tieGames += 1
		printScoreBoard()
		stillPlaying = askForAnotherGame()




