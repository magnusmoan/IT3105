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
        radius0 = radius = parameters['init_radius']
        learning_rate0 = learning_rate = parameters['init_learning_rate']

        cities = normalize_nodes(country)

        # Initialize neurons
        no_of_neurons = len(cities) * 3
        neurons = [[random(), random()] for _ in xrange(no_of_neurons)]

        # Uncomment the following line to initialize neurons in a circle
	#neurons = init_neurons(no_of_neurons) 

        # Draw the initialize situation
        graph = plot_graph(cities, neurons, country, 0)
        raw_input("See graph for the initial situation. Press any key to start running the algorithm.")

        # Set the parameters for the linear decay functions. Does currently not allow for exponential
        # decay functions.
        delta_learning = ( float(learning_rate0) - .01) / num_iterations
        delta_radius = radius0 / float(num_iterations)

	for r in xrange(1, num_iterations-1):

                # Update the graph every iteration
                if r % K == 0:
                    graph = update_graph(neurons, country, r, graph)
                    print "Current total TSP distance: ", calculate_travelers_distance(neurons)

                # Make sure radius is an integer
                radius = int(math.floor(radius))

                # Check each city, find the neuron closest to the city and update that neuron and its
                # neighbours. Neighbour defined as neuron within radius.
                for _, city in enumerate(cities):
		    update_weights(neurons, city, learning_rate, radius, no_of_neurons)

                # Update learning rate and radius
                learning_rate = decay_learning(learning_rate0, r, delta_learning)
                radius = decay_radius(radius0, r, delta_radius)

        # Force the neuron closest to each city to have the exact position of that city.
        for _, city in enumerate(cities):
            update_weights(neurons, city, 1, 0, no_of_neurons)
            update_graph(neurons, country, 100, graph)
