from input_handler import *
from utils import *

def backtracking(col, col_list, rows_set):
    if col == N:
        SOLUTIONS.append(map(lambda x: x + 1, col_list))
        return
 
    for row in rows_set:
        if not diagonal_conflict(row, col, col_list):
 
            col_list[col] = row
            rows_set.remove(row)
            backtracking(col + 1, col_list, rows_set)
            col_list[col] = -1
            rows_set.add(row)

    return
 
def main(starting_positions, unused_rows):
    starting_positions_without_neg = remove_all_negative(starting_positions)
 
    if starting_positions_valid(starting_positions_without_neg, N):
        print "Valid starting positions, starting backtracking search for feasable solution"
        backtracking(len(starting_positions_without_neg), starting_positions, rows_set)

SOLUTIONS = []
N = get_N_from_user()
starting_positions = subtract_one_from_list(get_starting_positions_from_user(N))
rows_set = get_all_numbers_not_used(starting_positions, N)
print starting_positions
main(starting_positions, rows_set)
print "Solutions: "
for solution in SOLUTIONS:
    print solution
print "Total number of solutions: " + str(len(SOLUTIONS))
