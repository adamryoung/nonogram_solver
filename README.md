Nonogram Puzzle Solver - HackED Beta 2020
by Adam Young and Nolan Shaw

Description:
Solves some, but definitely not all, 5x5 nonograms.

Running Instructions:
1. Download nonogram_solver.py, and gram1.txt into the same directory
2. Have the latest version of python installed with numpy and pygame libraries.
3. Open the terminal and navigate to the directory where nonogram_solver.py and gram1.txt are located.
4. Type "python nanogram_solver.py [optional-alternate-nanogram-filename-argument]"
   - This will run and solve the nanogram in gram1.txt by default or from the file specified in the optional command line argument.
  
Nonogram File Format (from gram1.txt)
The counters for the columns are specified in the first line, and the second line specifies the counters for the rows of the nanogram.
For each line the rows/columns are separated by a comma, and multiple numbers for a single row/column are separated with a space.
