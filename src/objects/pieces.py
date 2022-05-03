from objects.shapes import piece_shape, piece_colors

class Pieces:
    """Luokka, joka kuvaa yhtä palikkaa ja sen arvoja

    Attributes:
        x_row: Paikka x-akselilla
        y_row: Paikka y-akselilla
        shape: Palikan muoto
        color: Palikan väri
        rotation: Palikan suunta
    """
    def __init__(self, x_row, y_row, shapenumber):
        """Luokan konstruktori, joka luo uuden palasen

        args:
            x_row: Paikka x-akselilla
            y_row: Paikka y-akselilla
            shapenumber: Palikan numero
        """
        self.x_row = x_row
        self.y_row = y_row
        self.shape = piece_shape(shapenumber)
        self.color = piece_colors(shapenumber)
        self.rotation = 0
