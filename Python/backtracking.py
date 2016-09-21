from time import time
from input_handler import *
from utils import *

def backtracking(col, col_list, rows_set):
    if col == N:
        SOLUTIONS.append(col_list[:])
        #SOLUTIONS.append(map(lambda x: x + 1, col_list))
        return
 
    for row in rows_set:
        if no_diagonal_conflict(row, col, col_list):
            col_list.append(row)
            rows_set.remove(row)
            backtracking(col + 1, col_list, rows_set)
            rows_set.add(row)
            del col_list[-1]
    return
 
def main(starting_positions):
    rows_set = get_all_numbers_not_used(starting_positions, N)
    if starting_positions_valid(starting_positions, N):
        print "Valid starting positions, starting backtracking search for feasable solution"
        backtracking(len(starting_positions), starting_positions, rows_set)

SOLUTIONS = []
N = get_N_from_user()
starting_positions = subtract_one_from_list(starting_positions_backtracking_algorithm(N))
start = time()
main(starting_positions)
print "Solutions: "
for solution in SOLUTIONS:
    print solution
print "Total number of solutions: " + str(len(SOLUTIONS))
print "Time used: " + str(time() - start)
