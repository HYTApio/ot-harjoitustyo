import unittest
from pieces import *
from shapes import *

class TestPieces(unittest.TestCase):
    def setUp(self):
        self.piece=Pieces(5, 0, 1)
    
    def test_get_shape_works(self):
        test_shape = get_shape()
        shapenumber = 0
        for i in range(7):
            if piece_shape(i)==test_shape.shape:
                shapenumber = i


        self.assertEqual(test_shape.x, 5)
        self.assertEqual(test_shape.y, 0)
        self.assertEqual(test_shape.color, piece_colors(shapenumber))
        self.assertEqual(test_shape.shape, piece_shape(shapenumber))