def is_legal_int(string):
    try:
        i = int(string)
        return True
    except:
        return False


def get_N_from_user():
    n = raw_input("N: ")
    if is_legal_int(n):
        return int(n)
    else:
        print "The provided value for n isn't an legal integer. Please enter another value."
        return get_N_from_user()

# Detects wether or not the elements of a list is within the valid range
def list_elements_in_range(li, minimum, maximum):
    for element in li:
        if int(element) < minimum or int(element) > maximum:
            print str(element) + "is not within the valid range (" + str(minimum) + "-" + str(maximum) + ")"
            return False
    return True

# Returns a list given from the user. Will fill the list with 1's of the number of 
# elements given by the user is less than n. 
def get_starting_positions_from_user(n):
    try:
        starting_positions = map(int, raw_input("Enter starting positions: ").split())
    except ValueError:
        print "One or more of the provided values was not an integer"
        return get_starting_positions_from_user(n)

    if len(starting_positions) > n:
        print "Cannot provide more starting positions than the value of n."
        return get_starting_positions_from_user(n)

    return starting_positions

def starting_positions_heuristic_algorithms(n):
    starting_positions = get_starting_positions_from_user(n)
    while not list_elements_in_range(starting_positions, 1 ,n):
        starting_positions = get_starting_positions_from_user(n)
    if len(starting_positions) < n:
        for _ in range(len(starting_positions), n):
            valid_starting_positions.append(1)

    return valid_starting_positions

def starting_positions_backtracking_algorithm(n):
    starting_positions = get_starting_positions_from_user(n)
    while not list_elements_in_range(starting_positions, 0, n):
        starting_positions = get_starting_positions_from_user(n)

    for index, element in enumerate(starting_positions):
        if element == 0:
            return starting_positions[:index]

    return starting_positions


