import math
from time import time
from random import Random, random
from utils import is_diagonal_conflict, diagonal_conflict_count,fitness,generate_mirror_solution
from input_handler import get_N_from_user, get_starting_positions_from_user

N = get_N_from_user()
SOLUTIONS = set([])
MAX_FIT = N*(N-1)/2
dt = 0.1
POPULATION_FACTOR = 1000
TEMP_0 = 1000
TEMP_T = 0.0001
R = Random()

def swap_attacked_queen(col_list):
	attacked_queen_index = []
	for c,r in enumerate(col_list):
		if is_diagonal_conflict(r,c,col_list): attacked_queen_index.append(c)
	if len(attacked_queen_index) == 0: return col_list
	i1,i2 = R.randint(0,len(attacked_queen_index)-1),R.randint(0,N-1)
	while (i1 == i2): i2 = R.randint(0,N-1)
	col_list[i1], col_list[i2] = col_list[i2], col_list[i1]
	return col_list

def get_initial_population(user_input=None):
	population = []
	if user_input != None: population.append(user_input)
	for i in range(N*POPULATION_FACTOR):
		col_list = [i for i in range(N)]
		R.shuffle(col_list)
		population.append(col_list)
	return population

def simmulated_annealing(pop):
	n = 0
	t = TEMP_0
	x = pop.pop()
	while (t > TEMP_T):
		y = swap_attacked_queen(x)
		fit_x,fit_y = fitness(x,MAX_FIT), fitness(y,MAX_FIT)
		prob = math.exp(-(fit_y-fit_x)/t)
		if fit_y >= fit_x or p > R.random():
			x = y
			if fitness(x,MAX_FIT) == MAX_FIT: 
				SOLUTIONS.add(tuple(x))
				SOLUTIONS.add(generate_mirror_solution(x,N))
				x = pop.pop()
		t = t - dt
		print "Iteration",n," Temp:",t," Num solutions:",len(SOLUTIONS)
		n += 1
	
if __name__=='__main__':
	start_time = time()
	initial_population = get_initial_population()
	simmulated_annealing(initial_population)
	end_time = time()
	print "\nFound", len(SOLUTIONS), "solutions in",end_time-start_time,"seconds"
