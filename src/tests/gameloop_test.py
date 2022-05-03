import unittest
import services.gameloop
from services.pieces_service import *
from objects.shapes import *
from services.grid import *


class TestScores(unittest.TestCase):
    def setUp(self):
        self.gameloop = services.gameloop.GameLoop()
    
    def test_fall(self):
        self.assertEqual(self.gameloop._fall(5000), True)
        self.assertEqual(self.gameloop._fall(49), False)
    
    def test_free_space(self):
        alku = self.gameloop._piece.y_row
        self.gameloop._free_space((0, -1, 0))
        self.assertEqual(self.gameloop._piece.y_row, alku)

        self.gameloop._piece.y_row+=5
        piece_position = piece_positions(self.gameloop._piece)
        for square in piece_position:
            position = (square[0], square[1])
            self.gameloop._locked_positions[position] = self.gameloop._piece.color
        self.gameloop._grid = create_grid(self.gameloop._locked_positions)
        self.gameloop._free_space((0, -1, 0))
        self.assertEqual(self.gameloop._piece.y_row, 4)
    
    def test_change(self):
        uusi = self.gameloop._next_piece
        self.gameloop._change()
        self.assertEqual(uusi, self.gameloop._piece)
        self.assertEqual(False, self.gameloop._change_piece)


