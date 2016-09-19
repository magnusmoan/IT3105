SHORT_TERM = {}
SOLUTIONS = []

N = 4
MAX_FITNESS = (N*(N-1))/2
MAX_NUMBER_OF_ITERATIONS = 100


def uniquefy_input(user_input):
    all_numbers = [i for i in range(N)]
    unused_numbers = []
    used_numbers = []
    occurences = {}

    for el1 in user_input:
        if el1 not in occurences:
            occurences[el1] = 0
            used_numbers.append(el1)
            for el2 in user_input:
                if el2 == el1:
                    occurences[el1] += 1

    unused_numbers = list(set(all_numbers) - set(used_numbers))
    for index, element in enumerate(user_input):
        if element in occurences and occurences[element] > 1:
            user_input[index] = unused_numbers[0]
            del unused_numbers[0]
            occurences[element] -= 1

    return tuple(user_input)


def fitness(solution):
    conflicts = 0
    for row, col in enumerate(solution):
        conflicts += diagonal_conflict_count(row, col, solution)
    return MAX_FITNESS - conflicts


def diagonal_conflict_count(row, col, solution):
    conflicts = 0
    for c_col, c_row in enumerate(solution[col:],col):
        if (c_row == row and c_col == col):
            continue

        if abs(c_row - row) == abs(c_col - col):
            conflicts += 1

    return conflicts

print fitness((1,0,3,2))


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





