import unittest
from grid import *


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.window = (800, 700)
        self.locked_positions = {(5, 18): (127, 255, 0), (6, 18): (127, 255, 0), (4, 19): (127, 255, 0), (5, 19): (127, 255, 0)}
    
    def test_draw_grid_works(self):
        grid = create_grid(self.locked_positions)
        self.assertEqual(grid[18][5], (127, 255, 0))
