import utils
import sys

EXPONENTIAL = 'Exponential'
LINEAR = 'Linear'
STATIC = 'Static'

decay_funcs = [LINEAR, EXPONENTIAL, STATIC]
no_of_funcs = len(decay_funcs)
options = ['Select Country', 'Set Learning Rate Decay Function', 'Set Neighborhood Decay Function', 'Set Number of Iterations',
        'Set Display Rate of D', 'Set Display Rate of Graph', 'Run Algorithm', 'Run Algorithm w/ Default Settings']

def user_quit(option):
    if option == "quit" or option == "q":
        return True
    return False

def get_rate_func(parameter_type):
    print "Please choose one of the following " + parameter_type + " decay functions:"
    for i in range(no_of_funcs):
        print str(i+1) +  ") " + decay_funcs[i]

    chosen = raw_input("Enter number (1 - " + str(no_of_funcs) + "): ")

    if user_quit(chosen):
        return -1

    if utils.is_int(chosen) and (int(chosen) >= 1 and int(chosen) <= no_of_funcs):
        print decay_funcs[int(chosen)-1] + " selected.\n"
        return decay_funcs[int(chosen)-1]
    elif len(chosen) == 0:
        return None
    else:
        print "You did not enter a valid number.\n"
        return get_rate_func(parameter_type)

def get_radius(explanation):
    print "Please enter the " + explanation + " radius as a percentage of total number of neurons"
    percentage = raw_input("% (0-100): ")

    if user_quit(percentage):
        return -1

    if utils.is_float(percentage):
        print explanation.title() + " radius set to " + str(percentage) + "% of total number of neurons.\n"
        return float(percentage)
    elif len(percentage) == 0:
        return None
    else:
        print "You did not enter a valid number. \n"
        return get_starting_radius()

def get_learning_rate(explanation):
    print "Please enter the " + explanation + " learning rate."
    rate = raw_input("Learning Rate (0-1): ")

    if user_quit(rate):
        return -1

    if utils.is_float(rate) and float(rate) <= 1 and float(rate) > 0:
        print explanation.title() + " learning rate set to " + str(rate) + ".\n"
        return float(rate)
    elif len(rate) == 0:
        return None
    else:
        "You did not enter a value above 0 and below or equal to 1.\n"
        return get_learning_rate(explanation)


def get_exponential_rate(rate_type):
    print "Please enter exponential decay factor."
    factor = raw_input("Lambda (float > 0): ")

    if user_quit(factor):
        return -1

    if utils.is_float(factor) and float(factor) > 0:
        print "Exponential decay factor for " + rate_type + " set to " + factor + "\n"
        return float(factor)
    elif len(factor) == 0:
        print "Exponential decay factor for " + rate_type + " set to the default value found in main.py\n"
        return ""
    else:
        "You did not enter a valid decay factor."
        return get_exponential_rate(rate_type)

def get_func(rate_type):
    func = get_rate_func(rate_type)
    if func == -1:
        return func

    if rate_type == 'radius':
        interval_func = get_radius
    else:
        interval_func = get_learning_rate

    start_rate = interval_func("starting")

    if start_rate == -1:
        return start_rate

    if func == LINEAR:
        rate = interval_func("ending")

    elif func == EXPONENTIAL:
        rate = get_exponential_rate(rate_type)
    
    else:
        rate = None

    if rate == -1:
        return rate
    else:
        return (func, start_rate, rate)

def get_k():
    print "Please enter how often you want to display D (total distance)."
    k = raw_input("k number of rounds between: ")

    if user_quit(k):
        return -1

    if k.isdigit():
        print "k set to " + str(k) + ".\n"
        return int(k)

    else:
        print "You need to enter an integer. \n"
        return get_k()

def display_graph():
    print "Please enter how often you want to display the graph."
    k = raw_input("Number of iterations between each time the graph is shown: ")

    if user_quit(k):
        return -1

    if k.isdigit():
        print "The graph will be shown every " + k + " iterations.\n"
        return int(k)

    else:
        print "you need to enter an integer. \n"
        return display_graph()

def get_n():
    print "Please enter total number of iterations. \nAn iteration is defined as a complete pass over all cities."
    n = raw_input("N: ")
    if user_quit(n):
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

    if user_quit(country): 
        return -1
    
    try:
        a = utils.get_nodes(country)
        print "Setting " + country + " as country.\n"
        return country
    except:
        print "The country you entered does not exist in the database.\n"
        return get_country()


def get_input_parameters():
    no_of_options = len(options)

    parameters = {"n": None, "k": None, "l_r": None, "n_r": None, 
            "country": None, "init_learning_rate": None, "init_radius": None,
            "lambda_learning": None, "lambda_radius": None, "show_graph": None}

    while True:
        print "\nPlease select an option or enter \"q\" to exit: "

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
            value = get_func("learning")
        elif chosen == 3:
            chosen = "n_r"
            value = get_func("radius")
        elif chosen == 4:
            chosen = "n"
            value = get_n()
        elif chosen == 5:
            chosen = "k"
            value = get_k()
        elif chosen == 6:
            chosen = "show_graph"
            value = display_graph()
        elif chosen == 7:
            return parameters
        elif chosen == 8:
            return {"n": None, "k": None, "l_r": None, "n_r": None, 
                    "country": None, "init_learning_rate": None, "init_radius": None,
                    "lambda_learning": None, "lambda_radius": None, "show_graph": None}
        else:
            "Print invalid option chosen"

        if value == -1:
            return value

        parameters[chosen] = value

