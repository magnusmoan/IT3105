from time import time
from collections import deque
from utils import *
from input_handler import setup_heuristic_algorithm
from output_handler import show_solutions

###############################################
################### SETUP #####################
N, user_input, ROTATION_AND_MIRRORING_LEGAL = setup_heuristic_algorithm()
initial_board = tuple(uniquefy_input(subtract_one_from_list(user_input), N))
MAX_FITNESS = (N*(N-1))/2
SHORT_TERM_SIZE = N*10
SHORT_TERM = deque([], SHORT_TERM_SIZE)
SOLUTIONS = set([])
STEP_BY_STEP = []

# Stopping criterias
MAX_ITERATIONS = 200000  # Maximum allowed number of iterations
MAX_TIME = 150            # Maximum allowed running time in seconds

# Maximum number of iterations without improvement before we allow a tabu solution
MAX_ITERATIONS_WITHOUT_IMPROVEMENT = 5
###############################################


def tabu_search(curr_board):
    max_iterations_left = MAX_ITERATIONS_WITHOUT_IMPROVEMENT
    curr_best_fitness = fitness(curr_board, MAX_FITNESS)
    for iteration in xrange(MAX_ITERATIONS):

        # If we are searching for the first solution we add each step to the step by step list
        if len(SOLUTIONS) == 0:
            STEP_BY_STEP.append(curr_board)
        SHORT_TERM.append(curr_board)

        # If the current board is a solution, we add it to the solution set
        if curr_best_fitness == MAX_FITNESS:
            SOLUTIONS.add(curr_board) 
            if ROTATION_AND_MIRRORING_LEGAL:
                add_mirror_and_rotated_solutions(curr_board, N, SOLUTIONS)
            curr_best_fitness = 0

        # Find all neighbors. A neighbor is a board were one queen swap is made
        neighborhood = generate_neighborhood(curr_board)

        best_neighbor_fitness = 0
        for neighbor in neighborhood:
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

        if time() - start_time > MAX_TIME:
            return


def run():
    global start_time
    start_time = time()
    tabu_search(initial_board)
    show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start_time, N, False)

run()

