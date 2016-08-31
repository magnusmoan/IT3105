from copy import copy
from time import time

def diagonal_conflict(row, column, column_list):
    for current_column in xrange(column):
        current_row = column_list[current_column]
        if (current_row == row and current_column == column) or current_row == -1:
            continue

        if abs(current_row - row) == abs(current_column - column):
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
 
    for row in rows_set:
        if not diagonal_conflict(row, col, col_list):
 
            new_col_list = col_list[:]
            new_col_list[col] = row
            new_rows_set = set(rows_set)
            new_rows_set.remove(row)
 
            try_col(col + 1, new_col_list, new_rows_set)
 
 
def backtracking(starting_positions, rows_set):
    starting_positions_without_empty = remove_all_negative(starting_positions)
 
    if starting_positions_valid(starting_positions_without_empty, N):
        print "Valid starting positions, starting backtracking search for feasable solution"
        try_col(len(starting_positions_without_empty), starting_positions, rows_set)
 
def handle_user_input():
    starting_positions = map(int, raw_input("Enter starting positions: ").split())

    if len(starting_positions) == 0:
        starting_positions = [7, 5, 3, 1, 6, 8, 2, 0]

    n = len(starting_positions)

    starting_positions = map(lambda x: x - 1, starting_positions)
    all_num_below_n = [i for i in range(n)]
    rows_set = set(all_num_below_n) - set(starting_positions)

    return starting_positions, rows_set, n

COUNTER = 0
starting_positions, rows_set, N = handle_user_input()
start = time()
backtracking(starting_positions, rows_set)
totalTime = time() - start
print "Total number of solutions: " + str(COUNTER)
print "Time used: " + str(totalTime)
