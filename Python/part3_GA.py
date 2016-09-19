from time import time
from random import Random, random
from input_handler import get_N_from_user, get_starting_positions_from_user, diagonal_conflict, diagonal_conflict_count, duplicates_in_array_count

def fitness(row_list):
	conflicts = 0
	for col,row in enumerate(row_list):
		conflicts += diagonal_conflict_count(row,col,row_list)
		conflicts += duplicates_in_array_count(row_list)
	return MAX_FITNESS - conflicts

class Chromosome:
	
	def __init__(self, parent=None):
		if parent==None: 
			row_list = [i for i in range(N)]
			R.shuffle(row_list)
			self._value = row_list
		else: 
			self._value = self.crossover(parent[0],parent[1])
			self.mutate()
		self._fitness = fitness(self._value)

	def crossover(self, p1, p2):
		i = R.randint(1,N-2)
		a = p1._value[:i] + p2._value[i:]
		b = p2._value[:i] + p1._value[i:]
		return a if fitness(a) >= fitness(b) else b

	def mutate(self):
		r = Random()
		if r.random() < MUTATION_RATE:
			new_int = R.randint(0,N-1)
			index = R.randint(0,N-1)
			self._value[index] = new_int

	def print_chromosome(self):
		print self._value, "Fitness:", self._fitness 
	

def generate_initial_population(starting_positions):
	return [Chromosome() for i in range(POPULATION_SIZE)]

def genetic_algorithm(pop):
	t = 0
	solutions = []
	population = pop
	while (len(solutions) <= 20):
		print "Generating generation",t
		new_population = []
		for i in range(POPULATION_SIZE):
			x = population[R.randint(0,POPULATION_SIZE - 1)]
			y = population[R.randint(0,POPULATION_SIZE - 1)]
			child = Chromosome([x,y])
			new_population.append(child)
			print child._value, child._fitness
			if child._fitness == MAX_FITNESS: 
				print "Found solution:",child._value
				solutions.append(child._value)
		population = new_population
		t += 1
	
if __name__ == "__main__":
	
	#Global parametres
	R = Random()	
	N = 8 
	MUTATION_RATE = 0.05
	POPULATION_SIZE = 1000
	MAX_FITNESS = N*(N-1)/2
	PROBC = 0.8
	
	starting_positions, rows_set = [0,6,3,5,2,2,3,1], set([4,7])
	initial_population = generate_initial_population(starting_positions)
	genetic_algorithm(initial_population)
	

