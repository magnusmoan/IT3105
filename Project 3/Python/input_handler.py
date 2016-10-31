learning_rate_funcs = ['Linear', 'Exponential', 'Static']
no_of_funcs = len(learning_rate_funcs)

def get_learning_rate_func():
    print "Please choose one of the following learning rate decay functions:"
    for i in range(no_of_funcs):
        print str(i+1), ") " + learning_rate_funcs[i]

    chosen = raw_input("Enter number (1 - " + str(no_of_funcs) + "): ")

    if chosen == "quit" or chosen == "q" or len(chosen) == 0:
        return -1

    if chosen.isdigit() and (int(chosen) >= 1 and int(chosen) <= no_of_funcs):
        print learning_rate_funcs[int(chosen)-1]
        return learning_rate_funcs[int(chosen)-1]
    else:
        print "You did not enter a valid number. \n"
        return get_learning_rate_func()

def get_k():
    print "Please enter how often you want to display D (total distance)."
    k = raw_input("k: ")

    if k == "quit" or k == "q" or len(k) == 0:
        return -1

    if k.isdigit():
        return k

    else:
        print "You need to enter an integer. \n"
        return get_k()

get_learning_rate_func()
get_k()

