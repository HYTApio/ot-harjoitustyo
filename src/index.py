import pygame
from gameloop import GameLoop

def main():
    game = GameLoop()
    pygame.display.set_caption("Tetris")
    game.start()
if __name__ == "__main__":
    main()
