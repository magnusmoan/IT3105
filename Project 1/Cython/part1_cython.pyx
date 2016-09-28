from input_handler import get_N_from_user, get_starting_positions_from_user
from time import time
from utils import diagonal_conflict, starting_positions_valid

cdef try_col(int col, col_list, rows_set, int n):
    if col == n:
        global COUNTER
        COUNTER += 1
        solutions.append(col_list[:])
        return
 
    cdef int row
    for row in rows_set:
        if not diagonal_conflict(row, col, col_list, n):
 
            col_list[col] = row
            rows_set.remove(row)
            try_col(col + 1, col_list, rows_set, n)
            col_list[col] = -1
            rows_set.add(row)
    return
 
cdef backtracking(starting_positions, rows_set, int n):
    valid_start, number_of_placed_queens = starting_positions_valid(starting_positions, n)
    if valid_start:
        print "Valid starting positions, starting backtracking search for feasable solution"
        try_col(number_of_placed_queens, starting_positions, rows_set, n)

 
cdef int COUNTER = 0
cdef int n
solutions = []

n = get_N_from_user()
starting_positions, rows_set = get_starting_positions_from_user(n)

start = time()
backtracking(starting_positions, rows_set, n)
totalTime = time() - start
for solution in solutions:
    print map(lambda x: x+1, solution)
print "Total number of solutions: " + str(COUNTER)
print "Time used: " + str(totalTime)
