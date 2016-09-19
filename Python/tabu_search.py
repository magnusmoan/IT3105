from utils import fitness, diagonal_conflict_count

SHORT_TERM = {}
SOLUTIONS = []

N = 5
MAX_FITNESS = (N*(N-1))/2
MAX_NUMBER_OF_ITERATIONS = 100


print fitness((0,2,1,3,4), MAX_FITNESS)


def tabu_search(solution):
    if fitness(solution) == MAX_FITNESS:
        SOLUTIONS.append(solution)
        SHORT_TERM[solution] = MAX_FITNESS

    for _ in range(MAX_ITERATIONS):
        neighborhood = generate_neighborhood(solution)


def generate_neighborhood(solution):
    neighborhood = []

    for index1, element1 in enumerate(solution):
        for index2, element2 in enumerate(solution[index1+1:], index1+1):
            neighbor = solution[:index1] + (element2,) + solution[index1+1:index2] + (element1,) + solution[index2+1:]
            neighborhood.append(neighbor)
    return neighborhood





