from random import randint 

board=[]

def guessShip():

	for row in xrange(5):
		board.append([0] * 5)

	def printBoard():
		for row in board:
			print row

	printBoard() # Load board for the first time

	randrow = randint(1,5)
	randcol = randint(1,5)

	for i in xrange(3):
		guessrow = int(raw_input("Guess Row: "))
		guesscol = int(raw_input("Guess Col: "))

		if (guessrow == randrow and guesscol == randcol):
			print "Bravo !! You sinked ship "
			break
			won=True

		else:
			if guessrow not in range(0,5) or guesscol not in range(0,5):
				print "Out of ocean !!!"
			elif board[guessrow][guesscol] == 1:
				print "You guessed it already."
			else:
				board[guessrow][guesscol] =1

		
		printBoard()

	print "Game Over - You failed !!!"


guessShip()
