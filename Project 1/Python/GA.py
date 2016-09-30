import math
from time import time
from random import Random, random
from utils import *
from input_handler import setup_heuristic_algorithm
from output_handler import show_solutions, print_current_status

###############################################
################### SETUP #####################
N, user_input, ROTATION_AND_MIRRORING_LEGAL = setup_heuristic_algorithm()
initial_board = tuple(uniquefy_input(subtract_one_from_list(user_input), N))
SOLUTIONS = set([])
STEP_BY_STEP = []
MAX_FITNESS = (N*(N-1))/2

# GA design parameters
MUTATION_RATE = 0.2
POP_SIZE = min(N*20, math.factorial(N))
NUM_SEL = int(POP_SIZE*.2)
CROSSOVER_RATE = max(1, int(math.ceil(N/10.0)))

# Stopping criterias
MAX_ITER = 10000   # Maximum allower number of iterations
MAX_TIME = 15    # Maximum allowed running time in seconds
###############################################


# Selection picks the NUM_SEL best individuals out of a given population
def selection(pop):
    pop.sort(key = lambda x: x[1], reverse=True)
    return pop[:NUM_SEL]

# There's a certain chance that an individual will mutate, which means 
# that 2 random queens are swapped.
def mutation(col_list):
	if random.random() < MUTATION_RATE:
	    i,j = random.randint(0,N-1), random.randint(0,N-1)
	    col_list[i], col_list[j] = col_list[j], col_list[i]
	return tuple(col_list)

# A new individual is created by performing a crossover of two individuals
def crossover(p1,p2): 
        swath = CROSSOVER_RATE
	i = random.randint(0,N - swath)
	s = range(i,i+swath)
	child = []
	for j in xrange(N):
		child.append(-1)
		if (j in s): child[j] = p1[j]
	for j in s:
		if p2[j] not in child: 
			V = p1[j]
			p2_Vi = p2.index(V)
			while (p2_Vi in s):
				V = p1[p2_Vi]
				p2_Vi = p2.index(V)
			child[p2_Vi] = p2[j]
	for j in xrange(N):
		if child[j] == -1: child[j] = p2[j]
	return tuple(child)


# An initial population is generated from the user input by finding neighbors
# of the input. A neighbor is defined as a board that contains 1 queen swap.
def generate_initial_population(user_input):
        STEP_BY_STEP.append(user_input)
	population = set([])
	curr_board = user_input
	while (len(population) < POP_SIZE):
		neighborhood = generate_random_neighborhood(curr_board, N, MAX_FITNESS, N)
		population.update(neighborhood)
                for curr_board in neighborhood:
                    curr_board = curr_board[0]
                    break
	return list(population)

def genetic_algorithm(initial_population):
	next_population = initial_population
        for t in range(MAX_ITER):
                no_of_solutions = len(SOLUTIONS) 
                print_current_status(MAX_TIME - (time() - start_time), MAX_ITER - t, no_of_solutions)
		population = selection(next_population)
		if (no_of_solutions == 0): STEP_BY_STEP.append(population[0][0])
		next_population = []
		n = len(population) - 1
		for i in xrange(POP_SIZE):
			x = population[random.randint(0,n)][0]
			y = population[random.randint(0,n)][0]
			z = crossover(x,y)
                        z_fitness = fitness(z, MAX_FITNESS)
                        if z_fitness != MAX_FITNESS:
			        z = mutation(list(z))
                                z_fitness = fitness(z, MAX_FITNESS)
			if z_fitness == MAX_FITNESS: 
                                if (len(SOLUTIONS) == 0): STEP_BY_STEP.append(z)
				SOLUTIONS.add(z)
                                if ROTATION_AND_MIRRORING_LEGAL:
                                    add_mirror_and_rotated_solutions(z, N, SOLUTIONS, MAX_FITNESS)

			elif ((z, z_fitness) not in next_population and z not in SOLUTIONS): 
				next_population.append((z, z_fitness))
                
                if time() - start_time > MAX_TIME:
                        return

def run():
    global start_time
    start_time = time()
    initial_population = generate_initial_population(initial_board)
    genetic_algorithm(initial_population)	
    show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start_time, N, False)
    
run()
