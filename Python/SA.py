import math
import random
from time import time
from utils import * 
from input_handler import setup_heuristic_algorithm
from output_handler import show_solutions

N, user_input, ROTATION_AND_MIRRORING_LEGAL = setup_heuristic_algorithm()
SOLUTIONS = set([])
STEP_BY_STEP = []
MAX_FITNESS = N*(N-1)/2
NEIGHBORHOOD_SIZE = MAX_FITNESS
MAX_ITERATIONS = 10
dt = 1
TEMP_0 = 100
TEMP_T = 0.0001
TESTER = 0

def swap_attacked_queen(col_list):
	attacked_queen_index = []
        y = col_list[:]
	for c,r in enumerate(col_list):
		if not no_diagonal_conflict(r,c,col_list): attacked_queen_index.append(c)
	if len(attacked_queen_index) == 0: return col_list
	i1,i2 = R.randint(0,len(attacked_queen_index)-1),R.randint(0,N-1)
	while (i1 == i2): i2 = R.randint(0,N-1)
	col_list[i1], col_list[i2] = col_list[i2], col_list[i1]
	return col_list


def simmulated_annealing(curr_board, runNo):
	t = TEMP_0
	while (t > TEMP_T):

            if len(SOLUTIONS) == 0:
                STEP_BY_STEP.append(curr_board)

	    neighbors = generate_neighborhood(curr_board)

            # Find the most promissing neighbor based on fitness
            best_neighbor_fitness = 0
            for neighbor in neighbors:
                if neighbor in SOLUTIONS:
                    continue
                curr_fitness = fitness(neighbor, MAX_FITNESS)
                if curr_fitness > best_neighbor_fitness:
                    best_neighbor = neighbor
                    best_neighbor_fitness = curr_fitness

                
            # Compare the best neighbor with the current board. 
            # If the neighbor is better we set it as the current board        
	    curr_board_fitness = fitness(curr_board,MAX_FITNESS)
            print curr_board, curr_board_fitness
            print best_neighbor, best_neighbor_fitness
            raw_input("")
            if best_neighbor_fitness >= curr_board_fitness:
                curr_board_fitness = best_neighbor_fitness
                curr_board = best_neighbor
                
            else:
                prob = math.exp(-(best_neighbor_fitness - curr_board_fitness)/t)
                if prob < random.random():
                    print prob
                    print "Random event happened!"
                    curr_board = list(curr_board)
                    random.shuffle(curr_board)
                    curr_board = tuple(curr_board)
                    curr_board_fitness = fitness(curr_board, MAX_FITNESS)

            if curr_board_fitness == MAX_FITNESS and curr_board not in SOLUTIONS:

                if len(SOLUTIONS) == 0:
                    STEP_BY_STEP.append(curr_board)

                SOLUTIONS.add(curr_board)
                #SOLUTIONS.add(generate_mirror_solution(curr_board, N))
                return
	    t = t - dt
            print "Run number: ", runNo, " Temp:",t

start_time = time()
initial_board = tuple(uniquefy_input(subtract_one_from_list(user_input),N))
for runNo in range(MAX_ITERATIONS):
    simmulated_annealing(initial_board, runNo)
show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start_time, N, False)

