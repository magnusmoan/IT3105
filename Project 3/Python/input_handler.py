learning_rate_funcs = ['Linear', 'Exponential']

def get_learning_rate_func():
    print "Please choose one of the following learning rate decay functions: \n"
    for i in range(learning_rate_funcs):
        print i, ") " + learning_rate_funcs[i]

    chosen = raw_input("Enter number (1 - " + len(learning_rate_funcs) + "): ")

    try:
        chosen = int(chosen)
        return

    if chosen.isint():
        return learning_rate_funcs[int(chosen)]

