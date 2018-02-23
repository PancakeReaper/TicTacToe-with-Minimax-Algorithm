from random import randint
import tictactoe as ttt

# Player 2 will always be a Bot

def findPossibleMoves():
	moves = []
	for r in range(3):
		for c in range(3):
			if ttt.board[r][c] == " ":
				moves.append([r,c])
	return moves

def findBestMove(cPlayer, returnPlay=True):
	if ttt.isGameOver():
		if cPlayer == 2:
			return -1
		else:
			return 1
	elif not ttt.isPlayPossible():
		return 0

	if cPlayer == 1:
		mark = "X"
		oPlayer = 2
	else:
		mark = "O"
		oPlayer = 1
	moveValues = {}
	moves = findPossibleMoves()
	for move in moves:
		ttt.board[move[0]][move[1]] = mark
		moveValues[str(move[0])+str(move[1])] = findBestMove(oPlayer, False)
		ttt.board[move[0]][move[1]] = " "
	if cPlayer == 1:
		return min(moveValues.values())
	else:
		maxValue = max(moveValues.values())
		if returnPlay:
			for k, v in moveValues.items():
				if v == maxValue:
					return k
		return maxValue

def startGame():
	whosTurn = randint(1,2)
	if whosTurn == 1:
		print("You go first!")
	else:
		print("Minimax Bot goes first!")
	ttt.boardToString()
	while not ttt.isGameOver() and ttt.isPlayPossible():
		if whosTurn == 1:
			ttt.makeMove(whosTurn)
			ttt.boardToString()
			if ttt.isGameOver():
				print("You win!!")
				ttt.playerOneWins += 1
			elif not ttt.isPlayPossible():
				print("Tie game!!")
				ttt.tieGames += 1
			whosTurn = 2
		else:
			bestMove = findBestMove(whosTurn)
			r = int(bestMove[0])
			c = int(bestMove[1])
			ttt.board[r][c] = "O"
			ttt.boardToString()
			if ttt.isGameOver():
				print("You Lose!!")
				ttt.playerTwoWins += 1
			elif not ttt.isPlayPossible():
				print("Tie Game!!")
				ttt.tieGames += 1
			whosTurn = 1

if __name__ == "__main__":
	stillPlaying = True
	while stillPlaying:
		startGame()
		ttt.printScoreBoard(True)
		stillPlaying = ttt.askForAnotherGame()

