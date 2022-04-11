from random import randint
from shapes import piece_colors, piece_shape


class Pieces:
    def __init__(self, x_row, y_row, shapenumber):
        self.x_row = x_row
        self.y_row = y_row
        self.shape = piece_shape(shapenumber)
        self.color = piece_colors(shapenumber)
        self.rotation = 0


def get_shape():
    return Pieces(5, 0, randint(0, 6))


def piece_positions(piece):
    positions = []
    shape = piece.shape
    y_row = 0
    rotation = piece.rotation % len(piece.shape)
    for i in shape[rotation]:
        x_row = 0
        for j in i:
            x_row += 1
            if j == "X":
                positions.append((piece.x_row+x_row, piece.y_row+y_row))
        y_row += 1

    helper = 0
    for i in positions:
        positions[helper] = (i[0] - 3, i[1] - 4)
        helper += 1

    return positions

def free_space(piece, grid):
    free_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    free_positions = [j for sub in free_positions for j in sub]
    piece_position = piece_positions(piece)
    for square in piece_position:
        if square not in free_positions:
            if square[1] > -1:
                return False
    return True

def game_lost(positions):
    for square in positions:
        if square[1] < 1:
            return True
    return False
