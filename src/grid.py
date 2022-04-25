import pygame

pygame.font.init()

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


def draw_window(window, grid, score):
    window.fill((0, 0, 0))
    for i in enumerate(grid):
        for j in enumerate(grid[i[0]]):
            pygame.draw.rect(window, grid[i[0]][j[0]], (PLAY_TOP_LEFT_X + j[0]*SQUARE_SIZE,
            PLAY_TOP_LEFT_Y + i[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
    draw_grid(window, grid)
    pygame.draw.rect(window, (128, 128, 128), (PLAY_TOP_LEFT_X,
    PLAY_TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 2)
    font = pygame.font.SysFont('comicsans', 40)
    label = font.render('Cleared rows: ' + str(score), 1, (255,255,255))
    score_x = PLAY_TOP_LEFT_X + 15
    score_y = PLAY_TOP_LEFT_Y - 75
    window.blit(label, (score_x, score_y))

def clear_rows(grid, locked):

    cleared = 0
    for row_number in range(len(grid)-1, -1, -1):
        row = grid[row_number]
        if (0,0,0) not in row:
            cleared += 1
            ind = row_number
            for number in range(len(row)):
                del locked[(number,row_number)]

    if cleared > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x_row, y_row = key
            if y_row < ind:
                new_key = (x_row, y_row + cleared)
                locked[new_key] = locked.pop(key)

    return cleared

def draw_next_shape(shape, window):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    shape_x = PLAY_TOP_LEFT_X + PLAY_WIDTH + 50
    shape_y = PLAY_TOP_LEFT_Y + PLAY_HEIGHT/2 - 40
    shaperotation = shape.shape[shape.rotation % len(shape.shape)]

    for i, row_number in enumerate(shaperotation):
        row = list(row_number)
        for j, symbol in enumerate(row):
            if symbol == 'X':
                pygame.draw.rect(window, shape.color, (shape_x + j*SQUARE_SIZE,
                shape_y + i*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
                pygame.draw.line(window, (128, 128, 128), (shape_x + j*SQUARE_SIZE, shape_y +
                i*SQUARE_SIZE), (shape_x + j*SQUARE_SIZE+SQUARE_SIZE, shape_y + i*SQUARE_SIZE))
                pygame.draw.line(window, (128, 128, 128), (shape_x + j*SQUARE_SIZE, shape_y +
                i*SQUARE_SIZE), (shape_x + j*SQUARE_SIZE, shape_y + i*SQUARE_SIZE+SQUARE_SIZE))

    window.blit(label, (shape_x + 10, shape_y - 30))
