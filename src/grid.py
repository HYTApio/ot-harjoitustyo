import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
PLAY_WIDTH = 300
PLAY_HEIGHT = 600
SQUARE_SIZE = 30
PLAY_TOP_LEFT_X = (WINDOW_WIDTH - PLAY_WIDTH) // 2
PLAY_TOP_LEFT_Y = WINDOW_HEIGHT - PLAY_HEIGHT


def create_grid(locked_positions):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    for i in enumerate(grid):
        for j in enumerate(grid[i[0]]):
            if (j[0], i[0]) in locked_positions:
                locked = locked_positions[(j[0], i[0])]
                grid[i[0]][j[0]] = locked
    return grid


def draw_grid(window, grid):
    for i in enumerate(grid):
        pygame.draw.line(window, (128, 128, 128), (PLAY_TOP_LEFT_X, PLAY_TOP_LEFT_Y +
        i[0]*SQUARE_SIZE), (PLAY_TOP_LEFT_X+PLAY_WIDTH, PLAY_TOP_LEFT_Y+i[0]*SQUARE_SIZE))
        for j in enumerate(grid[i[0]]):
            pygame.draw.line(window, (128, 128, 128), (PLAY_TOP_LEFT_X+j[0]*SQUARE_SIZE,
            PLAY_TOP_LEFT_Y), (PLAY_TOP_LEFT_X+j[0]*SQUARE_SIZE, PLAY_TOP_LEFT_Y+PLAY_HEIGHT))


def draw_window(window, grid):
    window.fill((0, 0, 0))
    for i in enumerate(grid):
        for j in enumerate(grid[i[0]]):
            pygame.draw.rect(window, grid[i[0]][j[0]], (PLAY_TOP_LEFT_X + j[0]*SQUARE_SIZE,
            PLAY_TOP_LEFT_Y + i[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
    draw_grid(window, grid)
    pygame.draw.rect(window, (128, 128, 128), (PLAY_TOP_LEFT_X,
    PLAY_TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 2)
