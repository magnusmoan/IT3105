from time import time
from input_handler import get_N_from_user, get_starting_positions_from_user

def diagonal_conflict(row, column, column_list):
    for c_col, c_row in enumerate(column_list):
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

def starting_positions_valid(starting_positions, n):
    number_of_placed_queens = len(starting_positions)

    if duplicates_in_array(starting_positions):
        print "Duplicates"
        return False

    for column in range(number_of_placed_queens):
        if diagonal_conflict(starting_positions[column], column, starting_positions):
            print "Diagonal conflict"
            return False

    return True

 
def try_col(col, col_list, rows_set):
    if col == N:
        global COUNTER
        COUNTER += 1
        print map(lambda x: x + 1, col_list)
        return
 
    for row in rows_set:
        if not diagonal_conflict(row, col, col_list):
 
            col_list[col] = row
            rows_set.remove(row)
            try_col(col + 1, col_list, rows_set)
            col_list[col] = -1
            rows_set.add(row)

    return
 
 
def backtracking(starting_positions, rows_set):
    starting_positions_without_empty = remove_all_negative(starting_positions)
    print starting_positions_without_empty
 
    if starting_positions_valid(starting_positions_without_empty, N):
        print "Valid starting positions, starting backtracking search for feasable solution"
        try_col(len(starting_positions_without_empty), starting_positions, rows_set)
 

COUNTER = 0
N = get_N_from_user()
starting_positions, rows_set = get_starting_positions_from_user(N)
start = time()
backtracking(starting_positions, rows_set)
totalTime = time() - start
print "Total number of solutions: " + str(COUNTER)
print "Time used: " + str(totalTime)
