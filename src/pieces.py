from shapes import *
from random import randint

class Pieces(object):
    def __init__(self, x, y, shapenumber):
        self.x = x
        self.y = y
        self.shape = piece_shape(shapenumber)
        self.color = piece_colors(shapenumber)
        self.rotation = 0
    

def get_shape(): 
    return Pieces(5, 0, randint(0, 6))

def convert_shape_format(piece):
    positions = []
    shape = piece.shape
    y = 0
    for i in shape[0]:
        x = 0
        for j in i:
            x +=1
            if j=="X":
                positions.append((piece.x+x, piece.y+y))
        y += 1

    x = 0
    for i in positions:
        positions[x] = (i[0] - 3, i[1] - 4)
        x+=1

    return positions