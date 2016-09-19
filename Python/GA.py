import math
from time import time
from random import Random, random
from input_handler import diagonal_conflict_count

# Global parametres
MUTATION_RATE = 0.1
POP_SIZE = 1000
SEL_RATE = 0.5
N = 10
MAX_FITNESS = N*(N-1)/2
MAX_ITER = 100
R = Random()

def fitness(col_list):
	conflicts = 0
	for col, row in enumerate(col_list):
		conflicts += diagonal_conflict_count(row,col,col_list)
	return MAX_FITNESS - conflicts

def selection(pop):
	next_pop = [(fitness(pop[i]),pop[i]) for i in range(len(pop))]
	next_pop_sorted = sorted(next_pop,key=lambda x:x[0],reverse=True)
	next_pop_sorted_list = [elem[1] for elem in next_pop_sorted]
	return next_pop_sorted_list

def mutation(col_list):
	r = R.random()
	if r < MUTATION_RATE:
	    i,j = R.randint(0,N-1), R.randint(0,N-1)
	    col_list[i], col_list[j] = col_list[j], col_list[i]
	return col_list

def crossover(p1,p2): 
	swath = R.randint(2,math.floor(N/2))
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

def get_initial_population(user_input=None):
	population = []
	if user_input != None: population.append(user_input)
	for i in range(POP_SIZE):
		col_list = [i for i in range(N)]
		R.shuffle(col_list)
		population.append(col_list)
	return population
	

def genetic_algorithm(initial_population):
	t = 0
	solutions = set([])
	next_population = initial_population
	while (t < MAX_ITER):
		print "New generation",t
		population = selection(next_population)[:int(POP_SIZE*SEL_RATE)]
		next_population = []
		for i in range(POP_SIZE):
			x = population[R.randint(0,len(population)-1)]
			y = population[R.randint(0,len(population)-1)]
			z = crossover(x,y)
			z = mutation(z)
			if fitness(z) == MAX_FITNESS: 
				print "Found solution"
				solutions.add(tuple(z))
			next_population.append(z)
		t += 1
	return [len(solutions),solutions]

if __name__=='__main__': 
	start_time = time()
	initial_population = get_initial_population()
	num_solutions, solutions = genetic_algorithm(initial_population)
	end_time = time()
	
	for i in solutions:
		print i
	print "Completed. Found", num_solutions,"solutions in", end_time - start_time,"seconds"

	
