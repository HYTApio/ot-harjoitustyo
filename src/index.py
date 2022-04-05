import pygame
from grid import *
from pieces import *

def play():

    locked_positions = {}
    run = True
    piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3
 
    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > fall_speed:
            fall_time = 0
            piece.y += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

        piece_position = convert_shape_format(piece)

        for i in range(len(piece_position)):
            x, y = piece_position[i]
            if y > -1:
                grid[y][x] = piece.color

        draw_window(window, grid)
        pygame.display.update()

window = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Tetris")

if __name__ == "__main__":
    play()
