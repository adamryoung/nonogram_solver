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
    Variables:
    - x0, x1, xf and y0, y1, yf are iterations of the data as it is formatted.
    - xf, and yf are the final outputs which will equal col_counters, and
    row_counters, respectively, for the remainder of the program.
    e.g. A value of col_counters[1] = [1, 2] indicates that the second column
    contains a sequence of 1 consecutive active pixel, followed by 2 consecutive
    active pixels.
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
    return(xf, yf)  # outputs to (col_counters, row_counters)


def generate_nonogram_grid():
    """
    Creates a 5 by 5 matrix to represent the working solution for the nonogram.
    Where a 0 in the matrix represents an empty square that is undetermined, a 
    1 represents a filled in square, and a 2 represents a crossed out sqaure.
    On initialization all squares will be 0 (undetermined).
    """
    nonogram = np.zeros((5, 5), dtype=int)
    return(nonogram)


def nonogram_empty_full(col_counters, row_counters, nonogram):
    """
    Detects any rows or columns that are either completely full (counter = 5),
    or completely empty (counter = 0) and fills them with 1s and 2s, respectiv-
    ely. This handles the typical first step when solving a nonogram where you
    fill in the "obvious" rows and columns because they are either all X's or
    all filled in.
    """
    for i in range(5):
        if col_counters[i] == [0]:  # column with 0 filled
            nonogram[:, i] = [2]
    for j in range(5):
        if row_counters[j] == [0]:  # row with 0 filled
            nonogram[j, :] = [2]
    for i in range(5):
        if col_counters[i] == [5]:  # column with all 5 filled
            nonogram[:, i] = [1]
    for j in range(5):
        if row_counters[j] == [5]:  # row with all 5 filled
            nonogram[j, :] = [1]
    nonogram = nonogram_checker(col_counters, row_counters, nonogram)
    return(nonogram)



def nonogram_counter_space(col_counters, row_counters, nonogram):
    """
    Any row or column that requires five spaces to be filled, but only in the
    case where there are multiple numbers in counter for that row/col.
    e.g. col_counters[2] = [2, 2] <- in this case there must be five spaces to
    fill this in since an X must be inbetween the two 2's. The same applies for
    a row or column with [3, 1], [1, 3], or [1, 1, 1] as its counters.
    """
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
        if 5 - (sum(row_counters[i]) + len(row_counters[i]) - 1) == 0:
            index = 0
            for counter in row_counters[i]:
                for _ in range(counter):
                    nonogram[i, index] = 1
                    index += 1
                if index < 4:
                    nonogram[i, index] = 2
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
    return(nonogram_checker(col_counters, row_counters, nonogram))


def bufferer(col_counters, row_counters, nonogram):
    for i in range(5):
        # check for completed part of counter in a single column.
        # if nonogram[:, i].tolist()
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
    nonogram = bufferer(col_counters, row_counters, nonogram)

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
