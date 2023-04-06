class Piece:
	def __init__(self, colour, value):
		self.__colour = colour
		self.__value = value
	def __str__(self):
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
    
	def __repr__(self):
		return self.__str__()
    
	def get_colour(self):
		return self.__colour
    
	def set_colour(self, colour):
		self.__color = colour
    
	def get_piece_type(self):
		return self.__piece_type
    
	def set_piece_type(self, piece_type):
		self.__piece_type = piece_type

	
class Board:
	def __init__(self):
		self.board = self.set_board()

	def set_board(self):
		result = [[" " for _ in range(8)] for _ in range(8)]

		for i in range(0, 8):
			result[1][i] = Piece("black", 0)
			result[6][i] = Piece("white", 0)
		
		for i in range(1, 6):
			result[7][i - 1] = Piece("white", i)
			result[0][i - 1] = Piece("black", i)

		for i in range(1, 4):
			result[7][i - 1 + 5] = Piece("white", 4 - i)
			result[0][i - 1 + 5] = Piece("black", 4 - i)

		return result

	
	def legal_move(self, from_pos, to_pos, turn):
		if not (0 <= from_pos[0] <= 7 and 0 <= from_pos[1] <= 7 and
                0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7):
			return False
		chessPiece = self.board[from_pos[1]][from_pos[0]]

		if (chessPiece == " "):
		    return False
		if chessPiece.get_colour() == "black" and turn == True:
			return False
		elif chessPiece.get_colour() == "white" and turn == False:
			return False
		return True

	def make_move(self, from_pos, to_pos, turn):
		if (self.legal_move(from_pos, to_pos, turn)):
			piece = self.board[from_pos[1]][from_pos[0]]
			self.board[from_pos[1]][from_pos[0]] = " "
			self.board[to_pos[1]][to_pos[0]] = piece
			return True
		else:
			return False
	def play_game(self):
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
	def print_board(self):
		print("-----------------------------------------")
		for i in range(0, 8):
			for j in range(0, 8):
				print(f"| {self.board[i][j]}  ", end="")
			print("|")
			print("-----------------------------------------")

chessBoard = Board()
chessBoard.set_board()
chessBoard.print_board()
chessBoard.play_game()


