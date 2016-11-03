from random import random, choice
from utils import *
from graph_generator import plot_graph, update_graph
from time import time
import math

def init_neurons(no_of_neurons):
    neurons = []
    delta_deg = 2*math.pi / no_of_neurons
    deg = 0

    for i in xrange(no_of_neurons):
        y = .5 + .3 * math.sin(deg)
        x = .5 + .3 * math.cos(deg)
        deg += delta_deg
        neurons.append([x,y])

    return neurons


def find_closest_neuron(neurons, city, no_of_neurons):
	""" Returns index j of the neuron closest to city i """
	dist_list = [euclidean_distance(neurons[j], city) for j in xrange(no_of_neurons)]
        return dist_list.index(min(dist_list))

def update_weights(neurons, city, learning_rate, radius, no_of_neurons):
	""" The function finds the closest neuron j to city i, and its 
	neighborhood, and updates the neuron positions """
        j = find_closest_neuron(neurons, city, no_of_neurons)

        for i in xrange(j - radius, j + radius + 1):
            discount = 1.0 / ( abs(j - i) + 1 )
            index = i % no_of_neurons
            neurons[index][0] += learning_rate * discount * (city[0] - neurons[index][0])
            neurons[index][1] += learning_rate * discount * (city[1] - neurons[index][1])

def calculate_travelers_distance(neurons):
	bridge = euclidean_distance(neurons[0],neurons[-1])
	return sum([euclidean_distance(neurons[j], neurons[j+1]) for j in range(len(neurons) - 1)]) + bridge

def run(parameters):
        # Initialize parameters given from user
        num_iterations = parameters['n']
        K = parameters['k']
        country = parameters['country']

	decay_learning = parameters['l_r']
	decay_radius = parameters['n_r']
        learning_rate0 = learning_rate = parameters['init_learning_rate']

        cities = normalize_nodes(country)

        # Initialize neurons
        no_of_neurons = len(cities) * 3
        #neurons = [[random(), random()] for _ in xrange(no_of_neurons)]

        # Uncomment the following line to initialize neurons in a circle
	neurons = init_neurons(no_of_neurons) 

        # Draw the initialize situation
        plot_graph(cities, neurons, country, 0, "initial_plot")

        radius0 = radius = float(no_of_neurons) / parameters['init_radius']

        learning_func_name = decay_learning.__name__
        if learning_func_name == 'exponential':
            decay_learning = decay_learning(parameters['lambda_learning'])
        elif learning_func_name == 'linear':
            decay_learning = decay_learning(( float(learning_rate0) - parameters['learning_min_rate']) / num_iterations)

        radius_func_name = decay_radius.__name__
        if radius_func_name == 'exponential':
            decay_radius = decay_radius(parameters['lambda_radius'])
        elif radius_func_name == 'linear':
            decay_radius = decay_radius(radius0 / float(num_iterations))

        print radius0
        return
	for r in xrange(1, num_iterations-1):

                # Update the graph every iteration
                if r % K == 0:
                    print "Current total TSP distance: ", calculate_travelers_distance(neurons)

                if r == num_iterations / 2:
                    plot_graph(cities, neurons, country, r, "half_way_plot")

                # Make sure radius is an integer
                radius = int(math.floor(radius))

                # Check each city, find the neuron closest to the city and update that neuron and its
                # neighbours. Neighbour defined as neuron within radius.
                for _, city in enumerate(cities):
		    update_weights(neurons, city, learning_rate, radius, no_of_neurons)

                # Update learning rate and radius
                learning_rate = decay_learning(learning_rate0, r)
                radius = decay_radius(radius0, r)

        # Force the neuron closest to each city to have the exact position of that city.
        for _, city in enumerate(cities):
            update_weights(neurons, city, 1, 0, no_of_neurons)

        plot_graph(cities, neurons, country, num_iterations, "final_plot")
        print ""
