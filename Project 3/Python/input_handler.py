import utils
import sys

decay_funcs = ['Linear', 'Exponential', 'Static']
no_of_funcs = len(decay_funcs)
options = ['Select Country', 'Set Learning Rate Decay Function', 'Set Neighborhood Decay Function', 'Set Number of Iterations',
        'Set Display Rate of D', 'Run Algorithm', 'Run Algorithm w/ Default Settings']

def get_rate_func(parameter_type):
    print "\nPlease choose one of the following " + parameter_type + " decay functions:"
    for i in range(no_of_funcs):
        print str(i+1) +  ") " + decay_funcs[i]

    chosen = raw_input("Enter number (1 - " + str(no_of_funcs) + "): ")

    if chosen == "quit" or chosen == "q" or len(chosen) == 0:
        return -1

    if chosen.isdigit() and (int(chosen) >= 1 and int(chosen) <= no_of_funcs):
        print decay_funcs[int(chosen)-1] + " selected.\n"
        return decay_funcs[int(chosen)-1]
    else:
        print "You did not enter a valid number. \n"
        return get_rate_func(parameter_type)

def get_learning_rate_func():
    return get_rate_func("learning rate")

def get_neighborhood_rate_func():
    return get_rate_func("neighborhood")

def get_k():
    print "Please enter how often you want to display D (total distance)."
    k = raw_input("k number of rounds between: ")

    if k == "quit" or k == "q" or len(k) == 0:
        return -1

    if k.isdigit():
        print "k set to " + str(k) + ".\n"
        return int(k)

    else:
        print "You need to enter an integer. \n"
        return get_k()

def get_n():
    print "Please enter total number of iterations."
    n = raw_input("N: ")
    if n == "quit" or n == "q" or len(n) == 0:
        return -1

    if n.isdigit():
        print "Number of iterations set to " + str(n) + ".\n"
        return int(n)

    else:
        print "You need to enter an integer. \n"
        return get_n()

def get_country():
    print "Please enter the name of the country you want to run the SOM algorithm on."
    country = raw_input("Country name: ")

    if country == "quit" or country == "q" or len(country) == 0:
        print "True"
        return -1
    
    try:
        a = utils.get_nodes(country)
        print "Setting " + country + " as country.\n"
        return country
    except:
        print sys.exc_info()[0]
        print "The country you entered does not exist in the database.\n"
        return get_country()


def get_input_parameters():
    no_of_options = len(options)

    parameters = {"n": None, "k": None, "l_r": None, "n_r": None, 
            "country": None, "init_learning_rate": None, "init_radius": None}

    while True:
        print "Please select an option: "

        for i in range(no_of_options):
            print str(i+1) + ") " + options[i]

        chosen = raw_input("Enter number (1 - " + str(no_of_options) + "): ")
        print ""
        if chosen == 'q' or chosen == 'quit' or len(chosen) == 0:
            return -1

        if not chosen.isdigit():
            "Print invalid option chosen"
            continue
        else:
            chosen = int(chosen)

        if chosen == 1:
            chosen = "country"
            value = get_country()
        elif chosen == 2:
            chosen = "l_r"
            value = get_learning_rate_func()
        elif chosen == 3:
            chosen = "n_r"
            value = get_neighborhood_rate_func()
        elif chosen == 4:
            chosen = "n"
            value = get_n()
        elif chosen == 5:
            chosen = "k"
            value = get_k()
        elif chosen == 6:
            return parameters
        elif chosen == 7:
            return {"n": None, "k": None, "l_r": None, "n_r": None, 
                    "country": None, "init_learning_rate": None, "init_radius": None}
        else:
            "Print invalid option chosen"

        if value == -1:
            return value

        parameters[chosen] = value

