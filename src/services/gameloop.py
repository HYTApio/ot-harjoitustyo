import pygame

from services.grid import create_grid, clear_rows
from services.pieces_service import free_space, game_lost, get_shape, piece_positions
from ui.game_window import draw_next_shape, draw_window, draw_lose_screen
from repositories.scores_repositories import (scores_repository as default_scores_repository)

class GameLoop:
    """Luokka, jonka avulla pidetään peliä pystyssä

    Attributes:
        fall_speed: Palikoiden tippumisnopeus
        change_piece: Palan vaihtumista seuraava olio
        piece: Nykyinen tippuva pala
        locked_positions: Paikoillaan olevat palat
        grid: Pelikenttä
        score: Pistetilanne
        next_piece: Seuraava pala
        scores_repository: Tiedosto, jossa on high score

    """
    def __init__(self, scores_repository = default_scores_repository):
        """Luokan konstruktori, joka luo uuden pelin

        args:
            scores_repository: Tiedosto, jossa on highscore
        """
        self._fall_speed = 0.5
        self._change_piece = False
        self._piece = get_shape()
        self._locked_positions = {}
        self._grid = create_grid(self._locked_positions)
        self._score = 0
        self._next_piece = get_shape()
        self._scores_repository = scores_repository

    def start(self, window, highscore):
        """Pelin looppi, katsoo koko ajan jos jotain tapahtuu, loppuu
        jos pelaaja lopettaa tai häviää pelin

        Args:
            window: Peli-ikkunan koko
            highscore: Pelaajan paras pistetulos
        """
        clock = pygame.time.Clock()
        fall_time = 0
        while True:
            self._grid = create_grid(self._locked_positions)
            fall_time += clock.get_rawtime()
            if self._fall(fall_time):
                fall_time = 0
            clock.tick()
            if self._handle_events() is False:
                break
            self._draw_piece()
            if self._change_piece:
                self._change()
            if game_lost(self._locked_positions):
                draw_lose_screen(window, self._score)
                self._scores_repository.add_score(self._score)
                break
            draw_window(window, self._grid, self._score, highscore)
            draw_next_shape(self._next_piece, window)
            pygame.display.update()


    def _handle_events(self):
        """Katsoo mitä näppäimiä pelaaja painaa ja tekee tapahtumia sen mukaan

        Returns:
            False jos pelaaja poistuu
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._piece.x_row -= 1
                    change = (1, 0, 0)
                    self._free_space(change)

                elif event.key == pygame.K_RIGHT:
                    self._piece.x_row += 1
                    change = (-1, 0, 0)
                    self._free_space(change)

                elif event.key == pygame.K_UP:
                    self._piece.rotation = self._piece.rotation + 1 % len(self._piece.shape)
                    change = (0, 0, -1)
                    self._free_space(change)

                elif event.key == pygame.K_DOWN:
                    self._piece.y_row += 1
                    change = (0, -1, 0)
                    self._free_space(change)

            if event.type == pygame.QUIT:
                return False

    def _free_space(self, change):
        """Tarkistaa onko paikka mihin palikka liikkumassa täynnä
        ja jos on niin muuttaa takaisin lähtöpisteeseen

        args:
            change: Muutos palikan paikassa
        """
        if not free_space(self._piece, self._grid):
            self._piece.x_row += change[0]
            self._piece.y_row += change[1]
            self._piece.rotation = self._piece.rotation + change[2] % len(self._piece.shape)

    def _fall(self, falltime):
        """Liikuttaa ajan kanssa palikkaa, nopeuttaa tippumista tarkistaa voiko palikka tippua enää

        args:
            falltime: Kulunut aika ennen viime liikkumista

        returns:
            True jos palikka liikkuu
            False jos palikka ei liiku
        """
        if falltime/1000 > self._fall_speed:
            self._piece.y_row += 1
            if self._fall_speed > 0.2:
                self._fall_speed-=0.001
            if not free_space(self._piece, self._grid) and self._piece.y_row > 0:
                self._piece.y_row -= 1
                self._change_piece = True
            return True
        return False

    def _draw_piece(self):
        """Piirtää tipppuvan palasen
        """
        piece_position = piece_positions(self._piece)

        for position in enumerate(piece_position):
            x_row, y_row = position[1]
            if y_row > -1:
                self._grid[y_row][x_row] = self._piece.color

    def _change(self):
        """Vaihtaa palasen uuteen, lukitsee vanhan palasen pelikenttään ja
        tarkistaa tyhjentyykö rivejä
        """
        piece_position = piece_positions(self._piece)

        for square in piece_position:
            position = (square[0], square[1])
            self._locked_positions[position]=self._piece.color
        self._piece = self._next_piece
        self._next_piece = get_shape()
        self._change_piece = False
        self._score += clear_rows(self._grid, self._locked_positions)
