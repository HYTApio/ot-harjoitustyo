import pygame

pygame.font.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
PLAY_WIDTH = 300
PLAY_HEIGHT = 600
SQUARE_SIZE = 30
PLAY_TOP_LEFT_X = (WINDOW_WIDTH - PLAY_WIDTH) // 2
PLAY_TOP_LEFT_Y = WINDOW_HEIGHT - PLAY_HEIGHT

def draw_grid(window, grid):
    """Piirtää neliö taustan pelialueelle

    args:
        window: Peli-ikkunan koko
        grid: Pelialueen koko
    """
    for i in enumerate(grid):
        pygame.draw.line(window, (128, 128, 128), (PLAY_TOP_LEFT_X, PLAY_TOP_LEFT_Y +
        i[0]*SQUARE_SIZE), (PLAY_TOP_LEFT_X+PLAY_WIDTH, PLAY_TOP_LEFT_Y+i[0]*SQUARE_SIZE))
        for j in enumerate(grid[i[0]]):
            pygame.draw.line(window, (128, 128, 128), (PLAY_TOP_LEFT_X+j[0]*SQUARE_SIZE,
            PLAY_TOP_LEFT_Y), (PLAY_TOP_LEFT_X+j[0]*SQUARE_SIZE, PLAY_TOP_LEFT_Y+PLAY_HEIGHT))


def draw_window(window, grid, score, highscore):
    """Piirtää peli-ikkunan ja pistetilanteet

    args:
        window: Peli-ikkunan koko
        grid: Pelialue
        score: Nykyinen pelaajan pistetilanne
        highscore: Pelaajan paras pistetulos
    """
    window.fill((0, 0, 0))
    for i in enumerate(grid):
        for j in enumerate(grid[i[0]]):
            pygame.draw.rect(window, grid[i[0]][j[0]], (PLAY_TOP_LEFT_X + j[0]*SQUARE_SIZE,
            PLAY_TOP_LEFT_Y + i[0]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 0)
    draw_grid(window, grid)
    pygame.draw.rect(window, (128, 128, 128), (PLAY_TOP_LEFT_X,
    PLAY_TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 2)
    font = pygame.font.SysFont("comicsans", 40)
    label = font.render("Cleared rows: " + str(score), 1, (255,255,255))
    score_x = PLAY_TOP_LEFT_X + 15
    score_y = PLAY_TOP_LEFT_Y - 75
    window.blit(label, (score_x, score_y))
    label = font.render("High Score: " + str(highscore), 1, (255,255,255))
    score_x = PLAY_TOP_LEFT_X + 400
    score_y = PLAY_TOP_LEFT_Y - 75
    window.blit(label, (score_x, score_y))

def draw_next_shape(shape, window):
    """Piirtää seuraavan muodon

    args:
        window: Peli-ikkunan koko
        shape: Piirrettävä muoto
    """

    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (255,255,255))

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

def draw_lose_screen(window, score):
    """Piirtää häviö ikkunan kun peli loppuu

    args:
        window: Peli-ikkunan koko
        score: Pelaajan lopllinen pistetilanne
    """
    window.fill((0,0,0))
    font = pygame.font.SysFont("comicsans", 60, bold=True)
    label = font.render('YOU LOST! YOUR SCORE WAS ' + str(score), 1, (255,255,255))
    window.blit(label, (500 - (label.get_width() / 2), 400 - label.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)