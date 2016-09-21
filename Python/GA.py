import math
from time import time
from random import Random, random
from utils import diagonal_conflict_count,fitness,generate_mirror_solution,generate_neighborhood, uniquefy_input
from input_handler import get_N_from_user, starting_positions_heuristic_algorithms
from output_handler import show_solutions

N = get_N_from_user()
user_input = uniquefy_input(starting_positions_heuristic_algorithms(N),N)
STEP_BY_STEP = []
SOLUTIONS = set([])
MUTATION_RATE = 0.1
POP_SIZE = 1000
NUM_SEL = 100
MAX_FITNESS = (N*(N-1))/2
MAX_ITER = 100
R = Random()

def selection(pop):
	next_pop = [(fitness(pop[i],MAX_FITNESS),pop[i]) for i in range(len(pop))]
	next_pop_sorted = sorted(next_pop,key=lambda x:x[0],reverse=True)[:NUM_SEL]
	next_pop_sorted_list = [elem[1] for elem in next_pop_sorted]
	return next_pop_sorted_list

def mutation(col_list):
	r = R.random()
	if r < MUTATION_RATE:
	    i,j = R.randint(0,N-1), R.randint(0,N-1)
	    col_list[i], col_list[j] = col_list[j], col_list[i]
	return tuple(col_list)

def crossover(p1,p2): 
	swath = R.randint(1,math.floor(N/2))
	i = R.randint(0,N - swath)
	s = range(i,i+swath)
	child = []
	for j in range(N):
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
	for j in range(N):
		if child[j] == -1: child[j] = p2[j]
	return child


def generate_initial_population(user_input):
	population = set([])
	x = user_input
	while (len(population) < POP_SIZE):
		neighborhood = generate_neighborhood(tuple(x))
		for n in neighborhood:
			population.add(n)
		x = neighborhood[R.randint(0,len(neighborhood) - 1)]
	return list(population)

def genetic_algorithm(initial_population):
	t = 0
	next_population = initial_population
	while (t < MAX_ITER):
		print "New generation",t,". Number of solutions:", len(SOLUTIONS)
		population = selection(next_population)
		if (len(SOLUTIONS) == 0): STEP_BY_STEP.append(population[0])
		next_population = []
		n = len(population) - 1
		t += 1
		for i in range(POP_SIZE):
			x = population[R.randint(0,n)]
			y = population[R.randint(0,n)]
			z = crossover(x,y)
			z = mutation(z)
			if fitness(z,MAX_FITNESS) == MAX_FITNESS: 
				SOLUTIONS.add(z)
				SOLUTIONS.add(generate_mirror_solution(z,N))
			elif (z not in next_population and z not in SOLUTIONS): 
				next_population.append(z)

start = time()
initial_population = generate_initial_population(user_input)
genetic_algorithm(initial_population)	
show_solutions(STEP_BY_STEP,SOLUTIONS,time() - start)

"""
def get_initial_population(user_input=None):
	population = []
	if user_input != None: population.append(user_input)
	for i in range(POP_SIZE):
		col_list = [i for i in range(N)]
		R.shuffle(col_list)
		population.append(col_list)
	return population
"""
