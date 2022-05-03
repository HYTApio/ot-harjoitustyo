def create_grid(locked_positions):
    """Tekee tyhjän pelikentän ja lisää siihen kaikki lukitut palaset ja niiden värit

    args:
        locked_positions: Lukittujen palasten koordinaatit ja värit

    returns:
        täytetyn pelialueen
    """
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    for i in enumerate(grid):
        for j in enumerate(grid[i[0]]):
            if (j[0], i[0]) in locked_positions:
                locked = locked_positions[(j[0], i[0])]
                grid[i[0]][j[0]] = locked
    return grid

def clear_rows(grid, locked):
    """Tarkistaa täyttyikö vaakarivistä kaikki paikat ja jos täyttyi
    tyhjentää ja antaa pisteitä jokaisesta rivistä

    args:
        locked: lukittujen palikoiden sijainnit, joita muutetaan, jos rivejä
        tyhjennettiin
        grid: Pelikenttä, josta tarkistetaan onko rivit täynnä

    returns:
        kuinka monta riviä tyhjennettiin
    """
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
