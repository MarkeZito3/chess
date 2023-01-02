# Board
import os

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def valid_moves(self, board):
        # Este método debe ser implementado por las clases hijas
        pass

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "q" if self.color == "w" else "Q"

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "k" if self.color == "w" else "K"

class Torre(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "t" if self.color == "w" else "T"

class Caballo(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "c" if self.color == "w" else "C"

class Alfil(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "a" if self.color == "w" else "A"

class Peon(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "p" if self.color == "w" else "P"

    def valid_moves(self, board):
        moves = []

        # No puse el movimiento "captura al paso" o "peón al paso" porque no se me ocurría cómo hacerlo xd, después veo

        # Obtener la dirección en la que se mueve el peón
        direction = 1 if self.color == "w" else -1

        # Comprobar si hay una pieza enemiga en la diagonal derecha
        if self.col < 7 and board[self.row + direction][self.col + 1] != " " and board[self.row + direction][self.col + 1].color != self.color:
            moves.append((self.row + direction, self.col + 1))

        # Comprobar si hay una pieza enemiga en la diagonal izquierda
        if self.col > 0 and board[self.row + direction][self.col - 1] != " " and board[self.row + direction][self.col - 1].color != self.color:
            moves.append((self.row + direction, self.col - 1))

        # Comprobar si hay una casilla vacía delante del peón
        if board[self.row + direction][self.col] == " ":
            moves.append((self.row + direction, self.col))

        # Si el peón aún no se ha movido, también puede avanzar dos casillas
        if (self.color == "w" and self.row == 1) or (self.color == "b" and self.row == 6):
            if board[self.row + direction][self.col] == " " and board[self.row + direction * 2][self.col] == " ":
                moves.append((self.row + direction * 2, self.col))

        return moves


board = [
	["t", "c", "a", "q", "k", "a", "c", "t"],
	["p", "p", "p", "p", "p", "p", "p", "p"],
	[" ", " ", " ", " ", " ", " ", "P", " "],
	[" ", " ", " ", " ", " ", " ", " ", " "],
	[" ", " ", " ", " ", " ", " ", " ", " "],
	[" ", " ", " ", " ", " ", " ", " ", " "],
	["P", "P", "P", "P", "P", "P", "P", "P"],
	["T", "C", "A", "Q", "K", "A", "C", "T"],
]

if __name__ == "__main__":


    cont = 9
    for i in board:
        cont -= 1
        print("[",cont,"] ║ ",end="")
        print(i)
    print("══════╣═════════════════════════════════════════")
    print("[ X ] ║ ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']")

    # os.system("cls")
    cont = 9
    print(board[1][0])
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

    # for i in Peon("w",2,1).valid_moves(board):
    #     cont -= 1
    #     print("[",cont,"] ║ ",end="")
    #     print(i)
    print("══════╣═════════════════════════════════════════")
    print("[ X ] ║ ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']")