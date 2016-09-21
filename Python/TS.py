from time import time
from collections import deque
from utils import fitness, generate_mirror_solution, generate_neighborhood, subtract_one_from_list, uniquefy_input
from output_handler import show_solutions
from input_handler import get_N_from_user, starting_positions_heuristic_algorithms

N = get_N_from_user()
user_input = starting_positions_heuristic_algorithms(N)
MAX_FITNESS = (N*(N-1))/2
SHORT_TERM_SIZE = N*10
SHORT_TERM = deque([], SHORT_TERM_SIZE)
SOLUTIONS = set([])
STEP_BY_STEP = []

# Max number of iterations
MAX_ITERATIONS = 2000

# Maximum number of iterations without improvement before we allow a tabu solution
MAX_ITERATIONS_WITHOUT_IMPROVEMENT = 5



def tabu_search(curr_board):
    max_iterations_left = MAX_ITERATIONS_WITHOUT_IMPROVEMENT
    curr_best_fitness = fitness(curr_board, MAX_FITNESS)
    for iteration in xrange(MAX_ITERATIONS):
        print "Starting iteration number: " + str(iteration)

        # If we are searching for the first solution we add each step to the step by step list
        if len(SOLUTIONS) == 0:
            STEP_BY_STEP.append(curr_board)
        SHORT_TERM.append(curr_board)

        # If the current board is a solution, we add it to the solution set
        if curr_best_fitness == MAX_FITNESS:
            SOLUTIONS.add(curr_board) 
            mirror = generate_mirror_solution(curr_board, N)
            SOLUTIONS.add(mirror)
            curr_best_fitness = 0

        # Find all neighbors. A neighbor is a board were one queen swap is made
        neighborhood = generate_neighborhood(curr_board)

        best_neighbor_fitness = 0
        for _,neighbor in enumerate(neighborhood):
            if neighbor in SHORT_TERM or neighbor in SOLUTIONS:
                continue
            
            curr_fitness = fitness(neighbor, MAX_FITNESS)
            if curr_fitness > best_neighbor_fitness:
                best_neighbor_fitness = curr_fitness
                best_neighbor = neighbor

        # Check if the current best neighbor is better than the current solution
        if best_neighbor_fitness < curr_best_fitness:

            # Checks if the maximum number of iterations without improvement is reached. If so pick a tabu board
            if max_iterations_left == 0:
                curr_board = SHORT_TERM.popleft() 
                curr_best_fitness = fitness(curr_board, MAX_FITNESS)
                max_iterations_left = MAX_ITERATIONS_WITHOUT_IMPROVEMENT
            else:
                max_iterations_left -= 1
        else:
            curr_best_fitness = best_neighbor_fitness
            curr_board = best_neighbor



start = time()
tabu_search(tuple(uniquefy_input(subtract_one_from_list(user_input), N)))
show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start, N, False)

