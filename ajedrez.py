""" 
Pieces Classes
"""

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "q" if self.color == "w" else "Q"
        self.name = "Queen"

    def valid_moves(self, board):
        moves = []

        # Comprobar si hay casillas vacías en las ocho posiciones que rodean al rey
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue  # No se puede mover al mismo lugar
                row = self.row + row_offset
                col = self.col + col_offset
                if (row >= 0 and row <= 7) and (col >= 0 and col <= 7):  # Fuera del tablero
                    while (board[row][col] == " " or board[row][col].color != self.color): # Si al rededor está vacío o hay una pieza de otro color
                        moves.append((row, col))
                        if board[row][col] != " ":
                            break
                        if row_offset == 0 and col_offset == 0:
                            continue  # No se puede mover al mismo lugar
                        row += row_offset
                        col += col_offset
                        if (row < 0 or row > 7) or (col < 0 or col > 7):  # Fuera del tablero
                            break
                    row = self.row
                    col = self.col
        return moves

    def valid_moves_on_chess(self, board):
        dict_row = {
            0:8,
            1:7,
            2:6,
            3:5,
            4:4,
            5:3,
            6:2,
            7:1
        }
        dict_col = {
            0:"A",
            1:"B",
            2:"C",
            3:"D",
            4:"E",
            5:"F",
            6:"G",
            7:"H",
        }
        new_board = []
        for x in self.valid_moves(board):
            new_board.append((dict_row[x[0]], dict_col[x[1]]))
        return new_board

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "k" if self.color == "w" else "K"
        self.name = "King"

    def valid_moves(self, board):
        moves = []

        # Comprobar si hay casillas vacías en las ocho posiciones que rodean al rey
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue  # No se puede mover al mismo lugar
                row = self.row + row_offset
                col = self.col + col_offset
                if row < 0 or row > 7 or col < 0 or col > 7:  # Fuera del tablero
                    continue
                if board[row][col] == " " or board[row][col].color != self.color: # Si al rededor está vacío o hay una pieza de otro color
                    moves.append((row, col))

        return moves

    def valid_moves_on_chess(self, board):
        dict_row = {
            "0":8,
            "1":7,
            "2":6,
            "3":5,
            "4":4,
            "5":3,
            "6":2,
            "7":1
        }
        dict_col = {
            "0":"A",
            "1":"B",
            "2":"C",
            "3":"D",
            "4":"E",
            "5":"F",
            "6":"G",
            "7":"H",
        }
        new_board = []
        for x in self.valid_moves(board):
            new_board.append((str(dict_row[x[0]]), str(dict_col[x[1]])))
        return new_board

class Torre(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "t" if self.color == "w" else "T"
        self.name = "Torre"

    def valid_moves(self, board):
        moves = []

        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue  # No se puede mover al mismo lugar
                if row_offset != 0 and col_offset != 0: # Cualquiera de los dos debe ser 0 para que siga el camino vertical u horizontal
                    continue
                row = self.row + row_offset
                col = self.col + col_offset
                if (row >= 0 and row <= 7) and (col >= 0 and col <= 7):
                    while board[row][col] == " " or board[row][col].color != self.color:
                        moves.append((row, col))
                        if board[row][col] != " ":
                            break
                        row += row_offset
                        col += col_offset
                        if (row < 0 or row > 7) or (col < 0 or col > 7):
                            break
                    row = self.row
                    col = self.col
        return moves

    def valid_moves_on_chess(self, board):
        dict_row = {
            0:8,
            1:7,
            2:6,
            3:5,
            4:4,
            5:3,
            6:2,
            7:1
        }
        dict_col = {
            0:"A",
            1:"B",
            2:"C",
            3:"D",
            4:"E",
            5:"F",
            6:"G",
            7:"H",
        }
        new_board = []
        for x in self.valid_moves(board):
            new_board.append((dict_row[x[0]], dict_col[x[1]]))
        return new_board

class Caballo(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "c" if self.color == "w" else "C"

class Alfil(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "a" if self.color == "w" else "A"
        self.name = "Alfil"

    def valid_moves(self, board):
        moves = []

        for row_offset in [-1,1]:
            for col_offset in [-1,1]:
                row = self.row + row_offset
                col = self.col + col_offset
                if (row >=0 and row <=7) and (col >= 0 and col<= 7):
                    while board[row][col] == " " or board[row][col].color != self.color:
                        moves.append((row,col))
                        if board[row][col] != " ": # Para que no siga avanzando si ya comió a una pieza enemiga
                            break
                        row += row_offset
                        col += col_offset
                        if (row < 0 or row > 7) or (col < 0 or col > 7):
                            break
                row = self.row
                col = self.col
        return moves

    def valid_moves_on_chess(self, board):
        dict_row = {
            0:8,
            1:7,
            2:6,
            3:5,
            4:4,
            5:3,
            6:2,
            7:1
        }
        dict_col = {
            0:"A",
            1:"B",
            2:"C",
            3:"D",
            4:"E",
            5:"F",
            6:"G",
            7:"H",
        }
        new_board = []
        for x in self.valid_moves(board):
            new_board.append((dict_row[x[0]], dict_col[x[1]]))
        return new_board


class Peon(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = "p" if self.color == "w" else "P"
        self.name = "Peon"

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

    def valid_moves_on_chess(self, board):
        dict_row = {
            0:8,
            1:7,
            2:6,
            3:5,
            4:4,
            5:3,
            6:2,
            7:1
        }
        dict_col = {
            0:"A",
            1:"B",
            2:"C",
            3:"D",
            4:"E",
            5:"F",
            6:"G",
            7:"H",
        }
        new_board = []
        for x in self.valid_moves(board):
            new_board.append((dict_row[x[0]], dict_col[x[1]]))
        return new_board

board = [
	["t", "c", "a", "q", "k", "a", "c", "t"],
	["p", "p", "p", "p", "p", "p", "p", "p"],
	[" ", " ", " ", " ", " ", " ", " ", " "],
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