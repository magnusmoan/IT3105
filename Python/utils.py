def uniquefy_input(user_input, n):
    all_numbers = [i for i in range(n)]
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

    return user_input

def fitness(solution, max_fitness):
    conflicts = 0
    for col, row in enumerate(solution):
        conflicts += diagonal_conflict_count(row, col, solution)
    return max_fitness - conflicts


def diagonal_conflict_count(row, col, solution):
    conflicts = 0
    for c_col, c_row in enumerate(solution[col:],col):
        if (c_row == row and c_col == col):
            continue

        if abs(c_row - row) == abs(c_col - col):
            conflicts += 1

    return conflicts

def generate_mirror_solution(solution, n):
    solution = list(solution)
    mirror = [0 for _ in range(n)]
    n -= 1
    for index, element in enumerate(solution):
        mirror[n-index] = element

    return tuple(mirror)
