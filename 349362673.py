# Piece Class
class Piece:
	def __init__(self, colour, value):
		""" Initializes the encapsulated attributes colour and self """
		self.__colour = colour
		self.__value = value
		# end of __init__
	def __str__(self):
		""" Returns a string version of the Piece Object """
		if (self.__value == 0):
			if (self.__colour == "white"):
				value = "♟"
			else:
				value = "♙"
		elif (self.__value == 1):
			if (self.__colour == "white"):
				value = "♜"
			else:
				value = "♖"
		elif (self.__value == 2):
			if (self.__colour == "white"):
				value = "♞"
			else:
				value = "♘"
		elif (self.__value == 3):
			if (self.__colour == "white"):
				value = "♝"
			else:
				value = "♗"
		elif (self.__value == 4):
			if (self.__colour == "white"):
				value = "♛"
			else:
				value = "♕"
		else:
			if (self.__colour == "white"):
				value = "♚"
			else:
				value = "♔"

		return value
		# end of __str__
		
	def __repr__(self):
		""" Overrides the default representation to present a printable version of the Piece object """
		return self.__str__()
		# end of __repr__ 
		
	def get_colour(self):
		""" Getter method which can retrieve and return the encapsulated colour attribute """
		return self.__colour
		# end of get_colour
		
	def set_colour(self, colour):
		""" Setter method that sets the encapsulated colour attribute to the provided value """
		self.__color = colour
		# end of set_colour

	def get_piece_type(self):
		""" Getter method which retrieves the encapsulated piece_type attribute """
		return self.__piece_type
		# end of get_piece_type
    
	def set_piece_type(self, piece_type):
		""" Setter method that sets the encapsulated piece_type attribute """
		self.__piece_type = piece_type
		# end of set_piece_type

# End of Piece Class

# Board Class
class Board:
	def __init__(self):
		""" Initialization method which initializes the attribute board """
		self.board = self.set_board()
		# end of __init__

	def set_board(self):
		""" Sets the Chess Board to the starting position """
		result = [[" " for _ in range(8)] for _ in range(8)]

		# Intializes row of pawns 
		for i in range(0, 8):
			result[1][i] = Piece("black", 0)
			result[6][i] = Piece("white", 0)

		# Initializes the rest of the pieces
		for i in range(1, 6):
			result[7][i - 1] = Piece("white", i)
			result[0][i - 1] = Piece("black", i)

		for i in range(1, 4):
			result[7][i - 1 + 5] = Piece("white", 4 - i)
			result[0][i - 1 + 5] = Piece("black", 4 - i)

		return result
		# end of set_board

	
	def legal_move(self, from_pos, to_pos, turn):
		""" Checks square the piece the player has chosen contains a piece, and is the correct colour """
        # Checks if the move out of bounds
		if not (0 <= from_pos[0] <= 7 and 0 <= from_pos[1] <= 7 and
				0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7):
			return False
		chessPiece = self.board[from_pos[1]][from_pos[0]]

		# Checks if square chosen is empty
		if (chessPiece == " "):
			return False
		# Checks if piece chosen is the incorrect colour
		if chessPiece.get_colour() == "black" and turn == True:
			return False
		elif chessPiece.get_colour() == "white" and turn == False:
			return False
		return True
		# end of legal_move

	def make_move(self, from_pos, to_pos, turn):
		""" Checks if the move is legal, and then moves the piece to the chosen square. """
		if (self.legal_move(from_pos, to_pos, turn)):
			piece = self.board[from_pos[1]][from_pos[0]]
			self.board[from_pos[1]][from_pos[0]] = " "
			self.board[to_pos[1]][to_pos[0]] = piece
			return True
		else:
			return False
		# end of make_move
		
	def play_game(self):
		""" Runs a loop to allows a player to move pieces on a Chessboard until they choose to quit by entering -1 """
		print("You are now playing a game, enter -1 to quit. Otherwise enter any number.")
		choice = int(input())
		turn = True
		while (choice != -1):
			current_pos = [0,0]
			new_pos = [0,0]
			if (turn == True):
				print("White's move")
			else:
				print("Black's move")
	
			print("Enter the position of the piece you want to move")
			current_pos[0] = int(input())
			current_pos[1] = int(input())

			print("Enter the position you want to move the peice to")
			new_pos[0] =  int(input())
			new_pos[1] = int(input())

			if (self.make_move(current_pos, new_pos, turn)):
				if (turn):
					turn = False
				else:
					turn = True
				self.print_board()
			else:
				print("illegal move")
			
			
			print("Enter -1 to quit, otherwise enter any number")
			choice = int(input())
			# end of play_game

	def print_board(self):
		""" Prints the Chessboard """
		print("-----------------------------------------")
		for i in range(0, 8):
			for j in range(0, 8):
				print(f"| {self.board[i][j]}  ", end="")
			print("|" + "  " + str(i))
			print("-----------------------------------------")
		print("  0    1    2    3    4    5    6    7")
		# end of print_board
# End of Board Class

chessBoard = Board()
chessBoard.set_board()
chessBoard.print_board()
chessBoard.play_game()
