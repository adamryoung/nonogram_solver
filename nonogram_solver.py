# nonogram_solver.py
import sys
import numpy as np


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
    return(nonogram)



            



if __name__ == "__main__":
    filename = read_command_line()
    (col_counters, row_counters) = read_nonogram(filename)
    # col_counters counts the number of activated pixels in each column of the
    # grid, and row_counters does the same for the rows. The nonogram will be
    # solved from this input data.
    nonogram = generate_nonogram_grid()
    nonogram = nonogram_empty_full(col_counters, row_counters, nonogram)


