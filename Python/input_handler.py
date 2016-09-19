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

def diagonal_conflict(row,column,column_list):
	for c_col, c_row in enumerate(column_list):
		if (c_row == row and c_col == column) or c_row == -1:
			continue
		if abs(c_row - row) == abs(c_col - column):
			return True
	return False

def diagonal_conflict_count(row,column,column_list):
	count = 0
	for c_col, c_row, in enumerate(column_list):
		if (c_row == row and c_col == column):
			continue
		if abs(c_row - row) == abs(c_col - column):
			count+=1
	return count

def duplicates_in_array_count(array):
	return abs (len(array) - len(set(array)))

