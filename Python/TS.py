from time import time
from collections import deque
from utils import fitness, generate_mirror_solution, generate_neighborhood, subtract_one_from_list, uniquefy_input
from output_handler import show_solutions
from input_handler import get_N_from_user, get_starting_positions_heuristic_algorithms

N = get_N_from_user()
user_input = get_starting_positions_heuristic_algorithms(N)
MAX_FITNESS = (N*(N-1))/2
SHORT_TERM_SIZE = N
SHORT_TERM = deque([], SHORT_TERM_SIZE)
SOLUTIONS = set([])
STEP_BY_STEP = []
NUMBER_OF_SOLUTIONS = 50
MAX_ITERATIONS = 1000


def tabu_search(solution):
    curr_best_fitness = fitness(solution, MAX_FITNESS)
    for _ in xrange(MAX_ITERATIONS):
        if len(SOLUTIONS) == 0:
            STEP_BY_STEP.append(solution)
        SHORT_TERM.append(solution)

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
            
            curr_fitness = fitness(neighbor, MAX_FITNESS)
            if curr_fitness > curr_best_fitness:
                curr_best_fitness = curr_fitness
                solution = neighbor


start = time()
tabu_search(tuple(uniquefy_input(subtract_one_from_list(user_input), N)))
show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start)

