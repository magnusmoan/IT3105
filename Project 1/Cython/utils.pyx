cimport cython
from libc.stdlib cimport malloc, free

cpdef diagonal_conflict(int row, int column, col_list, int n):
    cdef int c_col, c_row
    for c_col in xrange(n):
        c_row = col_list[c_col]
        if (c_row == row and c_col == column) or c_row == -1 :
            continue

        if abs(c_row - row) == abs(c_col - column):
            return True

    return False

cdef int duplicates_in_array(array, int n):
    cdef int i, j, curr_num
    for i in xrange(n):
        curr_num = array[i]
        for j in xrange(i+1, n):
            if curr_num == array[j]:
                return 1
    
    return 0

cdef int number_of_queens(array, int n):
    cdef int count, i
    count = 0
    for i in xrange(n):
        if array[i] != - 1:
            count += 1

    return count

cdef remove_all_negative(array, int n):
    cdef int number_of_unique, i, j, curr

    without_neg = [0 for _ in xrange(n)]
    j = 0

    for i in xrange(n):
        curr = array[i]
        if curr != -1:
            without_neg[j] = curr
            j += 1

    return without_neg

cpdef starting_positions_valid(starting_positions, int n):
    cdef int *test, column, row, number_of_queens_placed
    number_of_queens_placed = number_of_queens(starting_positions, n)
    without_neg = remove_all_negative(starting_positions, number_of_queens_placed)

    if duplicates_in_array(without_neg, number_of_queens_placed):
        print "Duplicates"
        return False, number_of_queens_placed
    
    for column in range(number_of_queens_placed):
        row = without_neg[column]
        if diagonal_conflict(row, column, without_neg, number_of_queens_placed):
            print "Diagonal conflict"
            return False, number_of_queens_placed

    return True, number_of_queens_placed
