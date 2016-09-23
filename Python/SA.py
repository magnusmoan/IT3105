import math
import random
from time import time
from operator import itemgetter
from utils import * 
from input_handler import setup_heuristic_algorithm
from output_handler import show_solutions

N, user_input, ROTATION_AND_MIRRORING_LEGAL = setup_heuristic_algorithm()
SOLUTIONS = set([])
STEP_BY_STEP = []
MAX_FITNESS = N*(N-1)/2
NEIGHBORHOOD_SIZE = int(N)

# Stopping criterias
MAX_ITERATIONS = 100  # Maximum allowed number of iterations
MAX_TIME = 1000         # Maximum allowed running time in seconds

# Temperature variables
dt = 0.001
TEMP_0 = 10
TEMP_T = 1
MAX_LOOP_ROUNDS = int((TEMP_0 - TEMP_T) / dt)

def simulated_annealing(curr_board, runNo):
	t = TEMP_0
        curr_board_fitness = fitness(curr_board, MAX_FITNESS)
        for _ in xrange(MAX_LOOP_ROUNDS):

            # If we are still looking for the first solution we add the current board to the
            # step by step list
            if len(SOLUTIONS) == 0:
                STEP_BY_STEP.append(curr_board)

            # We select the next neighbor by picking a random neighbor among the neighbors
            # that have the highest fitness
	    #neighbors = generate_neighborhood_with_fitness(curr_board, MAX_FITNESS)
            neighbors = generate_random_neighborhood(curr_board, NEIGHBORHOOD_SIZE, MAX_FITNESS, N)
                
            best_neighbor_fitness = 0
            for neighbor in neighbors:
                if neighbor[1] > best_neighbor_fitness:
                    best_neighbor_fitness = neighbor[1]
                    best_neighbor = neighbor[0]


            # Compare the best neighbor with the current board. 
            # If the neighbor is better we set it as the current board        
            if best_neighbor_fitness >= curr_board_fitness:
                curr_board_fitness = best_neighbor_fitness
                curr_board = best_neighbor
                
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
                    add_mirror_and_rotated_solutions(curr_board, N, SOLUTIONS)
                #print "Solution found. Temperature: ", t
                return
	    t -= dt

start_time = time()
initial_board = tuple(uniquefy_input(subtract_one_from_list(user_input),N))
for runNo in xrange(MAX_ITERATIONS):
    simulated_annealing(initial_board, runNo)
    if time() - start_time > MAX_TIME: break

show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start_time, N, False)

