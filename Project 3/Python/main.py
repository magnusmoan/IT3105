from SOM2 import run
from input_handler import get_input_parameters
from utils import linear, static, exponential

DEFAULT_N = 100
DEFAULT_K = 10
DEFAULT_L_RATE = .9
DEFAULT_MIN_L_RATE = 0.01
DEFAULT_RADIUS = 10.0
DEFAULT_L_DECAY_FUNC = linear
DEFAULT_R_DECAY_FUNC = linear
DEFAULT_EXPONENTIAL_RATE_RADIUS = 1000
DEFAULT_EXPONENTIAL_RATE_LEARNING = 1000
DEFAULT_COUNTRY = "Western-Sahara"

def set_default_parameters(parameters):
    if parameters['n'] == None:
        parameters['n'] = DEFAULT_N

    if parameters['k'] == None:
        parameters['k'] = DEFAULT_K

    if parameters['init_learning_rate'] == None:
        parameters['init_learning_rate'] = DEFAULT_L_RATE

    if parameters['init_radius'] == None:
        parameters['init_radius'] = DEFAULT_RADIUS

    learning_decay_func = parameters['l_r']
    if learning_decay_func == None:
        parameters['l_r'] = DEFAULT_L_DECAY_FUNC
    elif learning_decay_func == 'Linear':
        parameters['l_r'] = linear
    elif learning_decay_func == 'Exponential':
        parameters['l_r'] = exponential
    elif learning_decay_func == 'Static':
        parameters['l_r'] = static

    radius_decay_func = parameters['n_r']
    if radius_decay_func == None:
        parameters['n_r'] = DEFAULT_R_DECAY_FUNC
    elif radius_decay_func == 'Linear':
        parameters['n_r'] = linear
    elif radius_decay_func == 'Exponential':
        parameters['n_r'] = exponential
    elif radius_decay_func == 'Static':
        parameters['n_r'] = static

    if parameters['country'] == None:
        parameters['country'] = DEFAULT_COUNTRY

    if parameters['lambda_learning'] == None:
        parameters['lambda_learning'] = DEFAULT_EXPONENTIAL_RATE_LEARNING

    if parameters['lambda_radius'] == None:
        parameters['lambda_radius'] = DEFAULT_EXPONENTIAL_RATE_RADIUS

    parameters['learning_min_rate'] = DEFAULT_MIN_L_RATE

def main():
    print "#"*67
    print "#"*3 + " Self Organizing Map for solving Travelling Salesman Problem " + "#"*3
    print "#"*67
    

    parameters = get_input_parameters()

    while parameters != -1:
        set_default_parameters(parameters) 
        run(parameters)
        parameters = get_input_parameters()

main()
