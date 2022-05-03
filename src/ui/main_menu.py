import pygame
from services.gameloop import GameLoop
from repositories.scores_repositories import (scores_repository as default_scores_repository)

pygame.font.init()

def main_menu(window):
    """Main menua pyörittävä funktio, jos painaa jotain ohjaa itse peliin

    args:
        window: Näytön koko
    """
    run = True
    while run:
        window.fill((0,0,0))
        font = pygame.font.SysFont("comicsans", 60, bold=True)
        label = font.render('Press Any Key To Play', 1, (255,255,255))
        window.blit(label, (500 - (label.get_width() / 2), 400 - label.get_height() / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                window = pygame.display.set_mode((1000, 800))
                highscore = default_scores_repository.find_high_score()
                game = GameLoop()
                game.start(window, highscore)


    pygame.display.quit()
