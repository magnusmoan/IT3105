from time import time
from collections import deque
from utils import fitness, generate_mirror_solution, generate_neighborhood, subtract_one_from_list, uniquefy_input
from output_handler import show_solutions
from input_handler import get_N_from_user, starting_positions_heuristic_algorithms

N = get_N_from_user()
user_input = starting_positions_heuristic_algorithms(N)
MAX_FITNESS = (N*(N-1))/2
SHORT_TERM_SIZE = N*10
SHORT_TERM = deque([], SHORT_TERM_SIZE)
SOLUTIONS = set([])
STEP_BY_STEP = []
NUMBER_OF_SOLUTIONS = float("inf")
MAX_ITERATIONS = 1000
MAX_ITERATIONS_WITHOUT_IMPROVEMENT = 5



def tabu_search(curr_solution):
    max_iterations_left = MAX_ITERATIONS_WITHOUT_IMPROVEMENT
    curr_best_fitness = fitness(curr_solution, MAX_FITNESS)
    for iteration in xrange(MAX_ITERATIONS):
        print "Starting iteration number: " + str(iteration)
        if len(SOLUTIONS) == 0:
            STEP_BY_STEP.append(curr_solution)
        SHORT_TERM.append(curr_solution)

        if len(SOLUTIONS) == NUMBER_OF_SOLUTIONS:
            return

        if curr_best_fitness == MAX_FITNESS:
            SOLUTIONS.add(curr_solution) 
            mirror = generate_mirror_solution(curr_solution, N)
            SOLUTIONS.add(mirror)
            curr_best_fitness = 0
        neighborhood = generate_neighborhood(curr_solution)

        best_neighbor_fitness = 0
        for _,neighbor in enumerate(neighborhood):
            if neighbor in SHORT_TERM or neighbor in SOLUTIONS:
                continue
            
            curr_fitness = fitness(neighbor, MAX_FITNESS)
            if curr_fitness > best_neighbor_fitness:
                best_neighbor_fitness = curr_fitness
                best_neighbor = neighbor

        if best_neighbor_fitness < curr_best_fitness:
            if max_iterations_left == 0:
                curr_solution = SHORT_TERM.popleft() 
                curr_best_fitness = fitness(curr_solution, MAX_FITNESS)
                max_iterations_left = MAX_ITERATIONS_WITHOUT_IMPROVEMENT
            else:
                max_iterations_left -= 1
        else:
            curr_best_fitness = best_neighbor_fitness
            curr_solution = best_neighbor



start = time()
tabu_search(tuple(uniquefy_input(subtract_one_from_list(user_input), N)))
show_solutions(STEP_BY_STEP, SOLUTIONS, time() - start, N, False)

