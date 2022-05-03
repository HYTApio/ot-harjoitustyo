import unittest
from services.pieces_service import *
from objects.shapes import *
from services.grid import *


class TestPieces(unittest.TestCase):
    def setUp(self):
        self.piece = Pieces(5, 0, 1)
        self.locked = {}
        self.grid = create_grid(self.locked)

    def test_get_shape_works(self):
        test_shape = get_shape()
        shapenumber = 0
        for i in range(7):
            if piece_shape(i) == test_shape.shape:
                shapenumber = i

        self.assertEqual(test_shape.x_row, 5)
        self.assertEqual(test_shape.y_row, 0)
        self.assertEqual(test_shape.color, piece_colors(shapenumber))
        self.assertEqual(test_shape.shape, piece_shape(shapenumber))

    def test_piece_positions_works(self):
        self.piece.x_row-=1
        self.assertEqual(piece_positions(self.piece), [(3, -2), (4, -2), (3, -1), (4, -1)])
    
    def test_free_space(self):
        self.assertEqual(free_space(self.piece, self.grid), True)
        self.piece.y_row+=5
        piece_position = piece_positions(self.piece)
        for square in piece_position:
            position = (square[0], square[1])
            self.locked[position] = self.piece.color
        self.grid = create_grid(self.locked)
        self.assertEqual(free_space(self.piece, self.grid), False)
    
    def test_game_lost_works(self):
        self.assertEqual(game_lost(self.locked), False)
        piece_position = piece_positions(self.piece)
        for square in piece_position:
            position = (square[0], square[1])
            self.locked[position] = self.piece.color
        self.assertEqual(game_lost(self.locked), True)

        