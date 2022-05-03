import pygame
from ui.main_menu import main_menu

def main():
    pygame.display.set_caption("Tetris")
    window = pygame.display.set_mode((1000, 800))
    main_menu(window)

if __name__ == "__main__":
    main()
