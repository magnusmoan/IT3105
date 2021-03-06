import random as random

# Takes as input a list/tuple and an integer n (length of list/tuple)
# Returns a list where all duplicates have been exchanged for unused numbers in the
# range 0 to n
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

def no_diagonal_conflict(row, col, col_list):
    foo1 = row + col
    foo2 = col - row
    for c_col, c_row in enumerate(col_list):
        if c_col + c_row == foo1 or c_col - c_row == foo2:
            return False
    return True

def diagonal_conflict_count(row, col, solution):
    conflicts = 0
    for c_col, c_row in enumerate(solution[col:],col):
        if (c_row == row and c_col == col):
            continue

        if abs(c_row - row) == abs(c_col - col):
            conflicts += 1

    return conflicts


# Subtracts 1 from all numbers in a list and returns the modified list
def subtract_one_from_list(a):
    return [x - 1 for x in a]

# Adds 1 to all numbers in the given list and returns the new list
def add_one_to_list(a):
    return [x + 1 for x in a]

# Returns a list of all numbers in the range 0 to n that does not occur in a
def get_all_numbers_not_used(a, n):
    rows_set = set([i for i in range(n)]) - set(a)
    return rows_set

# Checks if there exists duplicates in a given array
def duplicates_in_array(array):
    return len(array) != len(set(array))

# Removes all negative numbers from an array
def remove_all_negative(array_with_zeros):
    non_zero_array = []
    for number in array_with_zeros:
        if number >= 0:
            non_zero_array.append(number)

    return non_zero_array

# Checks if a given starting position is valid for backtracking
def starting_positions_valid(starting_positions, n):
    if duplicates_in_array(starting_positions):
        print("Duplicates")
        return False

    for col, row in enumerate(starting_positions[1:], 1):
        if not no_diagonal_conflict(row, col, starting_positions[:col]):
            print("Diagonal conflict")
            return False

    return True

def generate_neighborhood(board):
    neighborhood = []
    for index1, element1 in enumerate(board):
        for index2, element2 in enumerate(board[index1+1:], index1+1):
            neighbor = board[:index1] + (element2,) + board[index1+1:index2] + (element1,) + board[index2+1:]
            neighborhood.append(neighbor)
    return neighborhood

def generate_random_neighborhood(board, neighborhood_size, max_fitness, n):
    neighborhood = set([])
    n -= 1

    for _ in range(neighborhood_size):
        x = random.randint(0, n)
        y = random.choice(list(range(0,x)) + list(range(x+1,n)))
        neighbor = list(board[:])
        neighbor[x], neighbor[y] = neighbor[y], neighbor[x]
        neighborhood.add((tuple(neighbor), fitness(neighbor, max_fitness)))

    return neighborhood

def generate_neighborhood_with_fitness(board, max_fitness, n):
    neighborhood = []
    n -= 1
    for index1, element1 in enumerate(board):
        for index2, element2 in enumerate(board[index1+1:], index1+1):
            neighbor = board[:index1] + (element2,) + board[index1+1:index2] + (element1,) + board[index2+1:]
            neighborhood.append((neighbor, fitness(neighbor, max_fitness)))
    return neighborhood

# Takes a list/tuple representing an n-queens solution as input and mirrors the solution
# to create a new solution.
def generate_mirror_solution(solution, n):
    solution = list(solution)
    mirror = [0 for _ in range(n)]
    n -= 1
    for index, element in enumerate(solution):
        mirror[n-index] = element

    return tuple(mirror)

def rotate_right(solution, n):
    n -= 1
    rotated = list(solution)
    for col, row in enumerate(solution):
        rotated[n - row] = col
    return tuple(rotated)

def add_mirror_and_rotated_solutions(solution, n, solutions, max_fitness):
    mirror = generate_mirror_solution(solution, n)
    solution_rotated = rotate_right(solution, n)
    mirror_rotated = rotate_right(mirror, n)
    if fitness(solution_rotated, max_fitness) == max_fitness: solutions.add(solution_rotated)
    if fitness(mirror_rotated, max_fitness) == max_fitness: solutions.add(mirror_rotated)
    solutions.add(mirror)
