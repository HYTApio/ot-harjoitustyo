def piece_shape(shape_number):
    """Antaa palikan muodon

    args:
        shapenumber: Palikan numero, jonka muoto annetaan

    returns:
        Antaa palikan muodot
    """
    i_shape = [["....",
                "..X.",
                "..X.",
                "..X.",
                "..X."],
               ["....",
                "XXXX",
                "....",
                "...."]]
    o_shape = [[".....",
               ".....",
               ".XX..",
               ".XX.."]]
    z_shape = [["....",
                ".XX.",
                "..XX",
                "...."],
               ["..X.",
                ".XX.",
                ".X..",
                "...."]]
    s_shape = [["....",
                "..XX",
                ".XX.",
                "...."],
               [".X..",
                ".XX.",
                "..X.",
                "...."]]
    t_shape = [[".....",
                "..X..",
                ".XXX.",
                ".....",
                "....."],
               [".....",
                "..X..",
                "..XX.",
                "..X..",
                "....."],
               [".....",
                ".....",
                ".XXX.",
                "..X..",
                "....."],
               [".....",
                "..X..",
                ".XX..",
                "..X..",
                "....."]]
    l_shape = [["....",
                "..X.",
                "..X.",
                "..XX"],
               ["...X",
                ".XXX",
                "....",
                "...."],
               ["....",
                ".XX.",
                "..X.",
                "..X."],
               ["....",
                "....",
                ".XXX",
                ".X.."], ]
    j_shape = [[".....",
                "..X..",
                "..X..",
                ".XX.."],
               [".....",
                ".XXX.",
                "...X.",
                "....."],
               [".....",
                "..XX.",
                "..X..",
                "..X.."],
               [".....",
                ".X...",
                ".XXX.",
                "....."], ]
    shapes = [i_shape, o_shape, z_shape, s_shape, t_shape, l_shape, j_shape]
    return shapes[shape_number]


def piece_colors(shape_number):
    """Antaa palikan v??rin

    args:
        shape_number: Palikan numero, jonka v??ri annetaan

    returns:
        Antaa palikan v??rin
    """
    colors = [(0, 255, 255), (255, 255, 0), (255, 0, 0),
              (127, 255, 0), (255, 0, 255), (255, 128, 0), (0, 0, 255)]
    return colors[shape_number]
