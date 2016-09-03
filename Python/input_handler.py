def is_legal_int(string):
    try:
        i = int(string)
        if i >= 4:
            return True
        return False
    except:
        return False


def get_N_from_user():
    n = raw_input("N: ")
    if is_legal_int(n):
        return int(n)
    else:
        print "The provided value for n isn't an legal integer. Please enter another value."
        return get_N_from_user()

def get_starting_positions_from_user(n):
    starting_positions = map(int, raw_input("Enter starting positions: ").split())

    if len(starting_positions) > n:
        print "Cannot provide more starting positions than the value of n. Please enter new starting positions"
        get_starting_positions_from_user(n)
    elif len(starting_positions) < n:
        for _ in range(len(starting_positions), n):
            starting_positions.append(0)

    starting_positions = map(lambda x: x - 1, starting_positions)


    rows_set = set([i for i in range(n)]) - set(starting_positions)

    return starting_positions, rows_set