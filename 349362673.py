#REMEMBER TO ADD COMMENTS AND DOCUMENTATION
class Piece:
	def __init__(self, colour, position, value):
		self.colour = colour
		self.position = position
		self.value = value

	def __str__(self):
		if (value == 1):
			if (colour == "white"):
				value = "♟"
			else:
				value = "♙"
		elif (value == 2):
			if (colour == "white"):
				value = "♞"
			else:
				value = "♘"
		elif (value == 3):
			if (colour == "white"):
				value = "♝"
			else:
				value = "♗"
		elif (value == 4):
			if (colour == "white"):
				value = "♜"
			else:
				value = "♖"
		elif (value == 5):
			if (colour == "white"):
				value = "♛"
			else:
				value = "♕"
		else:
			if (colour == "white"):
				value = "♚"
			else:
				value = "♔"

		return f"{colour} {value}"

	def __repr__(self):
		return self.__str__()


class Board:
	def __init__(self):
		self.board = self.set_board()

	def set_board(self):
		result = [[" " for _ in range(8)] for _ in range(9)]

		pieces_white = ["♜","♞","♝","♛","♚","♝","♞","♜"]
		pieces_black = ["♖","♘","♗","♔","♕","♗","♘","♖"]

		for i in range(0, 8):
			result[1][i] = "♟"
			result[7][i] = "♙"
			
			result[0][i] = pieces_white[i]
			result[8][i] = pieces_black[i]

		return result

	def print_board(self):
		for i in range(0, 9):
			for j in range(0, 8):
				print(f"| {self.board[i][j]}  ", end="")
			print("|")
			print("-----------------------------------------")


chessBoard = Board()
chessBoard.set_board()
print(chessBoard.print_board())


