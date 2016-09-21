from time import time
from input_handler import starting_positions_backtracking_algorithm, get_N_from_user
from output_handler import show_solutions
from utils import no_diagonal_conflict, get_all_numbers_not_used, subtract_one_from_list, starting_positions_valid

N = get_N_from_user()
SOLUTIONS = []
STEP_BY_STEP = []

def backtracking(col, col_list, rows_set):

    (len(SOLUTIONS) == 0) and STEP_BY_STEP.append(col_list[:])

    if col == N:
        SOLUTIONS.append(col_list[:])
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

starting_positions = subtract_one_from_list(starting_positions_backtracking_algorithm(N))
start = time()
main(starting_positions)
show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start, N, True)
