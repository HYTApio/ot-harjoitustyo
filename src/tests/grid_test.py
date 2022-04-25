import unittest
from grid import *


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.window = (800, 700)
        self.locked_positions = {(5, 18): (127, 255, 0), (6, 18): (127, 255, 0), (4, 19): (127, 255, 0), (5, 19): (127, 255, 0), (4, 18): (127, 255, 0), (3, 18): (127, 255, 0), (2, 18): (127, 255, 0), (1, 18): (127, 255, 0), (0, 18): (127, 255, 0), (7, 18): (127, 255, 0), (8, 18): (127, 255, 0), (9, 18): (127, 255, 0),}
        self.grid = create_grid(self.locked_positions)

    def test_draw_grid_works(self):
        grid = create_grid(self.locked_positions)
        self.assertEqual(grid[18][5], (127, 255, 0))

    def test_clear_rows_work(self):
        self.assertEqual(clear_rows(self.grid,self.locked_positions), 1)
