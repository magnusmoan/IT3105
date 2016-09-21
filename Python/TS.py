from time import time
from collections import deque
from utils import *
from input_handler import get_N_from_user, get_starting_positions_from_user

N = get_N_from_user()
user_input = get_starting_positions_from_user(N)
MAX_FITNESS = (N*(N-1))/2
SHORT_TERM_SIZE = MAX_FITNESS*2*N
MAX_ITERATIONS = 10000
SHORT_TERM = deque([], SHORT_TERM_SIZE)
NUMBER_OF_SOLUTIONS = 5000
SOLUTIONS = set([])


def tabu_search(solution):
    curr_best_fitness = fitness(solution, MAX_FITNESS)
    for _ in xrange(MAX_ITERATIONS):

        if len(SOLUTIONS) == NUMBER_OF_SOLUTIONS:
            return

        if curr_best_fitness == MAX_FITNESS:
            SOLUTIONS.add(solution) 
            mirror = generate_mirror_solution(solution, N)
            SOLUTIONS.add(mirror)
        neighborhood = generate_neighborhood(solution)

        curr_best_fitness = 0
        for _,neighbor in enumerate(neighborhood):
            if neighbor in SHORT_TERM or neighbor in SOLUTIONS:
                continue
            
            SHORT_TERM.append(neighbor)
            curr_fitness = fitness(neighbor, MAX_FITNESS)

            if curr_fitness > curr_best_fitness:
                curr_best_fitness = curr_fitness
                solution = neighbor

def generate_neighborhood(solution):
    neighborhood = []

    for index1, element1 in enumerate(solution):
        for index2, element2 in enumerate(solution[index1+1:], index1+1):
            neighbor = solution[:index1] + (element2,) + solution[index1+1:index2] + (element1,) + solution[index2+1:]
            neighborhood.append(neighbor)
    return neighborhood

start = time()
tabu_search(tuple(uniquefy_input(subtract_one_from_list(user_input), N)))
for solution in SOLUTIONS:
    print solution
print "Number of solutions: " + str(len(SOLUTIONS))
print "Time used: " + str(time() - start)

