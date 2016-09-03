cimport cython
from libc.stdlib cimport malloc, free
from input_handler import get_N_from_user, get_starting_positions_from_user
from time import time

cdef diagonal_conflict(int row, int column, int *column_list, int n):
    cdef int c_col, c_row
    for c_col in range(n):
        c_row = column_list[c_col]
        if (c_row == row and c_col == column) or c_row == -1 :
            continue

        if abs(c_row - row) == abs(c_col - column):
            return True

    return False

def duplicates_in_array(array):
    return len(array) != len(set(array))

def remove_all_negative(array_with_zeros):
    non_zero_array = []
    for number in array_with_zeros:
        if number >= 0:
            non_zero_array.append(number)

    return non_zero_array

def starting_positions_valid(starting_positions):
    cdef int number_of_placed_queens = len(starting_positions)
    cdef int *test, column, row

    if duplicates_in_array(starting_positions):
        print "Duplicates"
        return False
    
    test = <int *>malloc(number_of_placed_queens*cython.sizeof(int))
    for i in xrange(number_of_placed_queens):
        test[i] = starting_positions[i]
    
    for column in range(number_of_placed_queens):
        row = starting_positions[column]
        if diagonal_conflict(row, column, test, number_of_placed_queens):
            print "Diagonal conflict"
            return False

    return True

cdef try_col(int col, int *col_list, rows_set):
    if col == N:
        global COUNTER
        COUNTER += 1
        #print map(lambda x: x + 1, col_list)
        return
 
    cdef int row
    for row in rows_set:
        if not diagonal_conflict(row, col, col_list, N):
 
            col_list[col] = row
            rows_set.remove(row)
            try_col(col + 1, col_list, rows_set)
            col_list[col] = -1
            rows_set.add(row)

    return
 
 
cdef backtracking(int *c_starting_positions, starting_positions, rows_set):
    starting_positions_without_empty = remove_all_negative(starting_positions)
 
    if starting_positions_valid(starting_positions_without_empty):
        print "Valid starting positions, starting backtracking search for feasable solution"
        try_col(len(starting_positions_without_empty), c_starting_positions, rows_set)
 
def handle_user_input():
    starting_positions = map(int, raw_input("Enter starting positions: ").split())

    if len(starting_positions) == 0:
        starting_positions = [7, 5, 3, 1, 6, 8, 2, 0]

    n = len(starting_positions)

    starting_positions = map(lambda x: x - 1, starting_positions)
    all_num_below_n = [i for i in range(n)]
    rows_set = set(all_num_below_n) - set(starting_positions)

    return starting_positions, rows_set, n

cdef int COUNTER = 0
cdef int N

N = get_N_from_user()

cdef int *c_starting_positions

starting_positions, rows_set = get_starting_positions_from_user(N)
c_starting_positions = <int *>malloc(len(starting_positions)*cython.sizeof(int))
for i in xrange(len(starting_positions)):
    c_starting_positions[i] = starting_positions[i]

start = time()
backtracking(c_starting_positions, starting_positions, rows_set)
totalTime = time() - start
free(c_starting_positions)
print "Total number of solutions: " + str(COUNTER)
print "Time used: " + str(totalTime)
