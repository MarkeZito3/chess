from ajedrez import *

def board_class_pieces(piece,row,col):
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
# print(board_class_pieces("j",0,0))
board_with_classes = board
# cont = 9

row = 0
col = 0
for i in board:
	# cont -= 1
	# print("[",cont,"] ║ ",end="")
	for x in i:
		print(f"[{x}]",end="")
		board_with_classes[row][col] = board_class_pieces(piece=x,row=row,col=col)
		col += 1
	row += 1
	col = 0
	print("")
# print("══════╣═════════════════════════════════════════")
# print("[ X ] ║ ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']")

print("")
print("========================================================")
print("")
for i in board_with_classes:
	for x in i:
		if x == " ":
			print(f"[{x}]",end="")
		else:
			print(f"[{x.symbol}]",end="")
	print("")

try:
	print(f'7A: {Peon("w",1,0).valid_moves(board)}')
except Exception as e:
	print("7A: error :v")
	print(e)

try:
	print(f'7B: {Peon("w",1,1).valid_moves(board)}')
except Exception as e:
	print("7B: error :v")
	print(e)