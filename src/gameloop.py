import pygame
from grid import create_grid, draw_window
from pieces import free_space, get_shape, piece_positions, game_lost

class GameLoop:
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__fall_time = 0
        self.__fall_speed = 0.2
        self.__change_piece = False
        self.__piece = get_shape()
        self.__locked_positions = {}
        self.__grid = create_grid(self.__locked_positions)
        self.__window = pygame.display.set_mode((800, 700))

    def start(self):
        while True:
            self.__grid = create_grid(self.__locked_positions)
            self.__fall_time += self.__clock.get_rawtime()
            self.__fall()
            self.__clock.tick()
            if self.__handle_events() is False:
                break
            self.__draw_piece()
            if self.__change_piece:
                self.__change()
            if game_lost(self.__locked_positions):
                break
            draw_window(self.__window, self.__grid)
            pygame.display.update()


    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.__piece.x_row -= 1
                    change = (1, 0, 0)
                    self.__free_space(change)

                elif event.key == pygame.K_RIGHT:
                    self.__piece.x_row += 1
                    change = (-1, 0, 0)
                    self.__free_space(change)

                elif event.key == pygame.K_UP:
                    self.__piece.rotation = self.__piece.rotation + 1 % len(self.__piece.shape)
                    change = (0, 0, -1)
                    self.__free_space(change)

                if event.key == pygame.K_DOWN:
                    self.__piece.y_row += 1
                    change = (0, -1, 0)
                    self.__free_space(change)

            elif event.type == pygame.QUIT:
                return False

    def __free_space(self, change):
        if not free_space(self.__piece, self.__grid):
            self.__piece.x_row += change[0]
            self.__piece.y_row += change[1]
            self.__piece.rotation = self.__piece.rotation + change[2] % len(self.__piece.shape)

    def __fall(self):
        if self.__fall_time/1000 > self.__fall_speed:
            self.__fall_time = 0
            self.__piece.y_row += 1
            if not free_space(self.__piece, self.__grid) and self.__piece.y_row > 0:
                self.__piece.y_row -= 1
                self.__change_piece = True

    def __draw_piece(self):
        piece_position = piece_positions(self.__piece)

        for position in enumerate(piece_position):
            x_row, y_row = position[1]
            if y_row > -1:
                self.__grid[y_row][x_row] = self.__piece.color

    def __change(self):
        piece_position = piece_positions(self.__piece)

        for square in piece_position:
            position = (square[0], square[1])
            self.__locked_positions[position]=self.__piece.color
        self.__piece = get_shape()
        self.__change_piece = False

if __name__ == "__main__":
    play = GameLoop()
    play.start()
