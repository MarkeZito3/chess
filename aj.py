from ajedrez import *
import copy

def dict_board_class(piece,row,col):
	position = {
		"t":Torre("w",row,col),
		"T":Torre("b",row,col),
		"c":Caballo("w",row,col),
		"C":Caballo("b",row,col),
		"a":Alfil("w",row,col),
		"A":Alfil("b",row,col),
		"q":Queen("w",row,col),
		"Q":Queen("b",row,col),
		"k":King("w",row,col),
		"K":King("b",row,col),
		"p":Peon("w",row,col),
		"P":Peon("b",row,col),
		" ":" "
	}
	return position[piece]

def board_classes(board=list[list]):

	""" 
		### board_classes(board)

		transforms the string piece in the board position as an object piece
		#### example:
		```
		>>> # Python console:
		>>>
		>>> board = [["K"],["k"]]
		>>> board_classes(board=board)
		[[<ajedrez.King object at 0x00000218A52658A0>], [<ajedrez.King object at 0x00000218A5265630>]]
		```
	"""

	board_with_classes = copy.deepcopy(board)

	row = 0
	col = 0
	for i in board:
		for x in i:
			board_with_classes[row][col] = dict_board_class(piece=x,row=row,col=col)
			col += 1
		row += 1
		col = 0
	return board_with_classes

if __name__ == "__main__":
	print("========================================================")
	print("")
	cont = 9
	for i in board_classes(board=board):
		cont-=1
		print(f"[{cont}]║",end="")
		for x in i:

			piece = x if x == " " else x.symbol
			print(f"[{piece}]", end="")

		print("")
	print("═══╣════════════════════════")
	print("[X]║[A][B][C][D][E][F][G][H]")
	print("========================================================")
	# print(board)
	print("1: ",Peon("w",1,0).valid_moves(board_classes(board)))
	print("2: ",Peon("w",1,1).valid_moves(board_classes(board)))
	print("3: ",Peon("w",1,2).valid_moves(board_classes(board)))
	print("4: ",Peon("w",1,3).valid_moves(board_classes(board)))
	print("5: ",Peon("w",1,4).valid_moves(board_classes(board)))
	print("6: ",Peon("w",1,5).valid_moves(board_classes(board)))
	print("7: ",Peon("w",1,6).valid_moves(board_classes(board)))
	print("8: ",Peon("w",1,7).valid_moves(board_classes(board)))
	print("========================================================")
	print("1: ",Peon("b",6,0).valid_moves(board_classes(board)))
	print("2: ",Peon("b",6,1).valid_moves(board_classes(board)))
	print("3: ",Peon("b",6,2).valid_moves(board_classes(board)))
	print("4: ",Peon("b",6,3).valid_moves(board_classes(board)))
	print("5: ",Peon("b",6,4).valid_moves(board_classes(board)))
	print("6: ",Peon("b",6,5).valid_moves(board_classes(board)))
	print("7: ",Peon("b",6,6).valid_moves(board_classes(board)))
	print("8: ",Peon("b",6,7).valid_moves(board_classes(board)))
