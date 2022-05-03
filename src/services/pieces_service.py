from random import randint
from objects.pieces import Pieces

def get_shape():
    """Antaa satunnaisen palan

    returns:
        Palauttaa satunnaisen palikan
    """
    return Pieces(5, 0, randint(0, 6))


def piece_positions(piece):
    """Antaa palikan koordinaatit

    args:
        piece: Palikka, jonka koordinaatit otetaan

    returns:
        Palauttaa palikan koordinaatit
    """
    positions = []
    shape = piece.shape
    y_row = 0
    rotation = piece.rotation % len(piece.shape)
    for i in shape[rotation]:
        x_row = 0
        for j in i:
            x_row += 1
            if j == "X":
                positions.append((piece.x_row+x_row, piece.y_row+y_row))
        y_row += 1

    helper = 0
    for i in positions:
        positions[helper] = (i[0] - 3, i[1] - 4)
        helper += 1

    return positions

def free_space(piece, grid):
    """Tarkistaa onko palikan paikka vapaana pelikentän lukituista koordinaateista

    args:
        piece: Palikka, jonka paikkaa tutkitaan onko vapaa
        grid: Pelialue josta tutkitaan onko palikan paikka vapaa

    returns:
        True, jos palikan paikassa ei ole lukittuja palikoita
        False, jos palikan paikassa on lukittuja palikoita
    """
    free_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    free_positions = [j for sub in free_positions for j in sub]
    piece_position = piece_positions(piece)
    for square in piece_position:
        if square not in free_positions:
            if square[1] > -1:
                return False
    return True

def game_lost(positions):
    """Tarkistaako häviääkö pelaaja pelin

    args:
        positions: paikat, missä on lukittuna paloja

    returns:
        True, jos palikat on yli pelikentän korkeuden
        False, jos kaikki palikat on pelikentällä
    """
    for square in positions:
        if square[1] < 1:
            return True
    return False
