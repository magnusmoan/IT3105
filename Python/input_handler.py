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

# Returns a list given from the user. Will fill the list with 1's of the number of 
# elements given by the user is less than n. 
def get_starting_positions_from_user(n):
    try:
        starting_positions = map(int, raw_input("Enter starting positions: ").split())
    except ValueError:
        print "One or more of the provided values was not an integer"
        get_starting_positions_from_user(n)

    if len(starting_positions) > n:
        print "Cannot provide more starting positions than the value of n."
        get_starting_positions_from_user(n)

    for element in starting_positions:
        if int(element) < 1 or int(element) > n:
            print str(element) + " is not within the valid range (1-" + str(n) + ")"
            get_starting_positions_from_user(n)

    if len(starting_positions) < n:
        for _ in range(len(starting_positions), n):
            starting_positions.append(1)

    return starting_positions

