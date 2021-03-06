import math
import random
from time import time
from utils import * 
from input_handler import setup_heuristic_algorithm
from output_handler import show_solutions, print_current_status

###############################################
################### SETUP #####################
N, user_input, ROTATION_AND_MIRRORING_LEGAL = setup_heuristic_algorithm()
initial_board = tuple(uniquefy_input(subtract_one_from_list(user_input),N))
SOLUTIONS = set([])
STEP_BY_STEP = []
MAX_FITNESS = N*(N-1)/2
NEIGHBORHOOD_SIZE = N

# Stopping criterias
MAX_ITERATIONS = 10000          # Maximum allowed number of iterations
MAX_TIME = 150                  # Maximum allowed running time in seconds
NO_NEW_SOLUTION_ROUND_LIMIT = 3 # Maximum number of iterations in a row without finding any new solutions

# Temperature variables
dt = 0.001
TEMP_0 = 10
TEMP_T = 0
MAX_LOOP_ROUNDS = int((TEMP_0 - TEMP_T) / dt)
###############################################


def simulated_annealing(curr_board, runNo):
	t = TEMP_0
        curr_board_fitness = fitness(curr_board, MAX_FITNESS)
        for _ in xrange(MAX_LOOP_ROUNDS):

            # If we are still looking for the first solution we add the current board to the
            # step by step list.
            if len(SOLUTIONS) == 0:
                STEP_BY_STEP.append(curr_board)

            # Generate neighbors to our current board. This is done by performing a single swap between
            # two queens in the current board. What queens that are swapped is random. 
            neighbors = generate_random_neighborhood(curr_board, NEIGHBORHOOD_SIZE, MAX_FITNESS, N)
                
            best_neighbor_fitness = 0
            for neighbor in neighbors:
                if neighbor[1] > best_neighbor_fitness:
                    best_neighbor_fitness = neighbor[1]
                    best_neighbor = neighbor[0]


            # Compare the best neighbor with the current board. 
            # If the neighbor is better we set it as the current board.
            if best_neighbor_fitness >= curr_board_fitness:
                curr_board_fitness = best_neighbor_fitness
                curr_board = best_neighbor
                
            # If the best neighbor is worse than our current board we might still set
            # the neighbor as the current board. This is decided by a probability function
            # defined below.
            else:
                prob = math.exp(-abs(best_neighbor_fitness - curr_board_fitness)/t)
                if prob < random.random():
                    for neighbor in neighbors: break
                    curr_board = neighbor[0]
                    curr_board_fitness = neighbor[1]

            # If the current boards fitness is equal to the maximum fitness it is a solution.
            # If we haven't seen the solution before we add it to the solutions set
            if curr_board_fitness == MAX_FITNESS and curr_board not in SOLUTIONS:

                if len(SOLUTIONS) == 0:
                    STEP_BY_STEP.append(curr_board)

                SOLUTIONS.add(curr_board)
                if ROTATION_AND_MIRRORING_LEGAL:
                    add_mirror_and_rotated_solutions(curr_board, N, SOLUTIONS, MAX_FITNESS)
                return
	    t -= dt


def run():
    start_time = time()
    no_of_solutions = 0
    rounds_without_solution_left = NO_NEW_SOLUTION_ROUND_LIMIT

    for execution_number in xrange(MAX_ITERATIONS):
        print_current_status(MAX_TIME - (time() - start_time), MAX_ITERATIONS - execution_number, len(SOLUTIONS))
        simulated_annealing(initial_board, execution_number)

        # The algorithm stops running if either we have used more time than
        # MAX_TIME or there have been more than NO_NEW_SOLUTION_ROUND_LIMIT
        # without a new solution.
        if time() - start_time > MAX_TIME: break
        if len(SOLUTIONS) - no_of_solutions == 0:
            rounds_without_solution_left -= 1
            if rounds_without_solution_left == 0: break
        else:
            rounds_without_solution_left = NO_NEW_SOLUTION_ROUND_LIMIT
        no_of_solutions = len(SOLUTIONS)
    show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start_time, N, False)

run()
