# nonogram_solver.py
import sys
import numpy as np
import pygame as pg

def read_command_line():
    """
    Reads command line for additional argument that specifies file to be read.
    "python3 nonogram_solver.py <filename.txt>"
    If no filename is specified the default filename "gram1.txt" is used instead.
    sys.argv[1] = "<filename.txt>" in the case of the example above.
    """
    try:
        return(sys.argv[1])
    except:
        return("gram1.txt")


def read_nonogram(filename):
    """
    From the selected filename (see read_command_line) this reads the input,
    and formats it into a list of lists for both the x and y counters.
    The counters are the numbers that indicate the number of activated pixels
    in each row (y) and each column (x).
    """
    file = open(filename)
    (x0, y0) = file.read().split('\n')
    file.close()
    x1 = x0.split(',')
    y1 = y0.split(',')
    xf = []
    yf = []
    for i in range(len(x1)):
        xf += [[int(j) for j in x1[i].split()]]
    for i in range(len(y1)):
        yf += [[int(j) for j in y1[i].split()]]
    return(xf, yf)


def generate_nonogram_grid():
    nonogram = np.zeros((5, 5), dtype=int)
    return(nonogram)


def nonogram_empty_full(col_counters, row_counters, nonogram): 
    for i in range(5):
        if col_counters[i] == [0]:
            nonogram[:, i] = [2]
    for j in range(5):
        if row_counters[j] == [0]:
            nonogram[j, :] = [2]
    for i in range(5):
        if col_counters[i] == [5]:
            nonogram[:, i] = [1]
    for j in range(5):
        if row_counters[j] == [5]:
            nonogram[j, :] = [1]
    nonogram = nonogram_checker(col_counters, row_counters, nonogram)
    return(nonogram)



def nonogram_counter_space(col_counters, row_counters, nonogram):
    for i in range(5):
        if 5 - (sum(col_counters[i]) + len(col_counters[i]) - 1) == 0:
            index = 0
            for counter in col_counters[i]:
                for _ in range(counter):
                    nonogram[index, i] = 1
                    index += 1
                if index < 4:
                    nonogram[index, i] = 2
                    index += 1
    nonogram = nonogram_checker(col_counters, row_counters, nonogram)
    return(nonogram)


def nonogram_3or4(col_counters, row_counters, nonogram):
    for i in range(5):
        if col_counters[i] == [3]:
            nonogram[2, i] = 1
        if row_counters[i] == [3]:
            nonogram[i, 2] = 1
        if col_counters[i] == [4]:
            nonogram[1:4, i] = [1]
        if row_counters[i] == [4]:
            nonogram[i, 1:4] = [1]
    nonogram = nonogram_checker(col_counters, row_counters, nonogram)
    return(nonogram)


def nonogram_checker(col_counters, row_counters, nonogram):

    for i in range(5):
        if sum(col_counters[i]) == nonogram[:, i].tolist().count(1):
            nonogram[:, i] = [2 if x == 0 else x for x in nonogram[:, i]]
        if sum(row_counters[i]) == nonogram[i, :].tolist().count(1):
            nonogram[i, :] = [2 if x == 0 else x for x in nonogram[i, :]]
    if np.count_nonzero(nonogram == 0) == 0:
        print(nonogram)
        print("Wowza!")
    return(nonogram)





if __name__ == "__main__":
    filename = read_command_line()
    (col_counters, row_counters) = read_nonogram(filename)
    # col_counters counts the number of activated pixels in each column of the
    # grid, and row_counters does the same for the rows. The nonogram will be
    # solved from this input data.
    nonogram = generate_nonogram_grid()
    nonogram = nonogram_empty_full(col_counters, row_counters, nonogram)
    nonogram = nonogram_counter_space(col_counters, row_counters, nonogram)
    nonogram = nonogram_3or4(col_counters, row_counters, nonogram)

    pg.init()
    display = pg.display.set_mode((500,500),0,32)
    WHITE = (255, 255, 255)
    GRAY = (120, 120, 120)
    BLACK = (0, 0, 0)

    display.fill(WHITE)

    for i in range(5):
        for j in range(5):
            if nonogram[j, i] == 0:
                pg.draw.rect(display, GRAY, (100 * i, 100 * j, 100, 100))
                pg.draw.rect(display, BLACK, (100 * i, 100 * j, 100, 100), width = 1)
            elif nonogram[j, i] == 1:
                pg.draw.rect(display, BLACK, (100 * i, 100 * j, 100, 100))
                pg.draw.rect(display, BLACK, (100 * i, 100 * j, 100, 100), width = 1)
            elif nonogram[j, i] == 2:
                pg.draw.rect(display, WHITE, (100 * i, 100 * j, 100, 100))
                pg.draw.rect(display, BLACK, (100 * i, 100 * j, 100, 100), width = 1)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()





