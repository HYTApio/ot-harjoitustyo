import pygame

window_width = 800
window_height = 700
play_width = 300 
play_height = 600 
square_size = 30
play_top_left_x = (window_width - play_width) // 2
play_top_left_y = window_height - play_height

def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid

def draw_grid(window, grid):
    for i in range(len(grid)):
        pygame.draw.line(window, (128,128,128), (play_top_left_x, play_top_left_y+i*square_size), (play_top_left_x+play_width, play_top_left_y+i*square_size))
        for j in range(len(grid[i])):
            pygame.draw.line(window, (128, 128, 128), (play_top_left_x+j*square_size, play_top_left_y),(play_top_left_x+j*square_size, play_top_left_y+play_height))

def draw_window(window, grid):
    window.fill((0, 0, 0))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(window, grid[i][j], (play_top_left_x + j*square_size, play_top_left_y + i*square_size, square_size, square_size), 0)
    draw_grid(window, grid)
    pygame.draw.rect(window, (128, 128, 128), (play_top_left_x, play_top_left_y, play_width, play_height), 2)
