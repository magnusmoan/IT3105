from SOM2 import run
from input_handler import get_input_parameters
from utils import linear, static, exponential

DEFAULT_N = 100
DEFAULT_K = 25
DEFAULT_L_RATE = .99
DEFAULT_RADIUS = 3
DEFAULT_L_DECAY_FUNC = linear
DEFAULT_R_DECAY_FUNC = linear
DEFAULT_EXPONENTIAL_RATE = 5
DEFAULT_COUNTRY = "Western-Sahara"

def set_default_parameters(parameters):
    print parameters
    if parameters['n'] == None:
        parameters['n'] = DEFAULT_N

    if parameters['k'] == None:
        parameters['k'] = DEFAULT_K

    if parameters['init_l_r'] == None:
        parameters['init_l_r'] = DEFAULT_L_RATE

    if parameters['init_radius'] == None:
        parameters['init_radius'] = DEFAULT_RADIUS


    learning_decay_func = parameters['l_r']
    if learning_decay_func == None:
        parameters['l_r'] = DEFAULT_L_DECAY_FUNC( parameters['init_l_r'] / parameters['n'] )
    elif learning_decay_func == 'Linear':
        parameters['l_r'] = linear(parameters['init_l_r'] / parameters['n'])
    elif learning_decay_func == 'Exponential':
        parameters['l_r'] = exponential( DEFAULT_EXPONENTIAL_RATE )
    elif learning_decay_func == 'Static':
        parameters['l_r'] = static

    learning_decay_func = parameters['n_r']
    if learning_decay_func == None:
        parameters['n_r'] = DEFAULT_L_DECAY_FUNC( parameters['init_radius'] / parameters['n'] )
    elif learning_decay_func == 'Linear':
        parameters['n_r'] = linear(parameters['init_radius'] / parameters['n'])
    elif learning_decay_func == 'Exponential':
        parameters['n_r'] = exponential( DEFAULT_EXPONENTIAL_RATE )
    elif learning_decay_func == 'Static':
        parameters['n_r'] = static

    if parameters['country'] == None:
        parameters['country'] = DEFAULT_COUNTRY


def main():
    print "#"*67
    print "#"*3 + " Self Organizing Map for solving Travelling Salesman Problem " + "#"*3
    print "#"*67
    

    parameters = get_input_parameters()

    while parameters != -1:
        set_default_parameters(parameters) 
        print parameters
        run(parameters)
        parameters = get_input_parameters()

main()
