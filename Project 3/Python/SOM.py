from random import random, choice
from utils import *
from graph_generator import plot_graph
from time import time
import math
import numpy as np

def init_neurons(no_of_neurons):
    neurons = []
    delta_deg = 2*math.pi / no_of_neurons
    deg = 0

    for i in xrange(no_of_neurons):
        y = .5 + .3 * math.sin(deg)
        x = .5 + .3 * math.cos(deg)
        deg += delta_deg
        neurons.append(np.array([x,y]))
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
            added_value = learning_rate * discount * np.subtract(city, neurons[index])
            neurons[index] = np.add(neurons[index], added_value)

def map_neurons_to_cities(neurons, cities):
        neuron_to_city = {}
        neurons_list = neurons[:]
        count = 0
        for city in cities:
            closest_neuron = find_closest_neuron(neurons_list, city, len(neurons_list))
            neurons_list[closest_neuron] = [1000,1000]
            neuron_to_city[closest_neuron] = city
        cities_in_order = []
        for index, neuron in enumerate(neurons):
            if index in neuron_to_city:
                cities_in_order.append(neuron_to_city[index])

        return cities_in_order

def calculate_travelers_distance(travelling_route):
	bridge = euclidean_distance(travelling_route[0], travelling_route[-1])
	return sum([euclidean_distance(travelling_route[j], travelling_route[j+1]) for j in range(len(travelling_route) - 1)]) + bridge

def run(parameters):
        # Initialize parameters given from user
        num_iterations = parameters['n']
        K = parameters['k']
        country = parameters['country']
        show_graph = parameters['show_graph']

	decay_learning = parameters['l_r']
	decay_radius = parameters['n_r']
        learning_rate0 = learning_rate = parameters['init_learning_rate']

        cities, (interval_x, interval_y), (min_x, min_y) = normalize_nodes(country)

        # Initialize neurons
        no_of_neurons = len(cities) * 2
        #neurons = [[random(), random()] for _ in xrange(no_of_neurons)]

        # Uncomment the following line to initialize neurons in a circle
	neurons = init_neurons(no_of_neurons) 

        # Draw the initialize situation
        travelling_route = map_neurons_to_cities(neurons, cities)
        travelling_route = nodes_to_coordinates(travelling_route, interval_x, interval_y, min_x, min_y)
        D = calculate_travelers_distance(travelling_route)
        plot_graph(cities, neurons, country, 0, "initial_plot", D)

        radius0 = radius = float(no_of_neurons) * (parameters['init_radius'] / float(100))

        print "\nCurrent parameters"
        print "Iterations:", num_iterations
        print "K:", K
        print "Graph display rate:", show_graph
        print "Country:", country
        print "Learning0:", learning_rate0
        print "Radius0:", radius0
        print "Learning func:", decay_learning.__name__
        print "Radius func:", decay_radius.__name__
        print "Learning min:", parameters['learning_min_rate']
        print "Radius min:", parameters['radius_min']
        print "Lambda learning:", parameters['lambda_learning']
        print "Lambda radius:", parameters['lambda_radius']
        raw_input("Press any button to start running the algorithm")
        start = time()

        learning_func_name = decay_learning.__name__
        if learning_func_name == 'exponential':
            decay_learning = decay_learning(parameters['lambda_learning'])
        elif learning_func_name == 'linear':
            decay_learning = decay_learning(( float(learning_rate0) - parameters['learning_min_rate']) / num_iterations)

        radius_func_name = decay_radius.__name__
        if radius_func_name == 'exponential':
            decay_radius = decay_radius(parameters['lambda_radius'])
        elif radius_func_name == 'linear':
            decay_radius = decay_radius( (radius0 - parameters['radius_min']) / float(num_iterations))
        
	for r in xrange(1, num_iterations-1):
                print "Iteration number:", r

                # Update the graph every iteration
                if r % K == 0:
                    travelling_route = map_neurons_to_cities(neurons, cities)
                    travelling_route = nodes_to_coordinates(travelling_route, interval_x, interval_y, min_x, min_y)
                    D = calculate_travelers_distance(travelling_route)
                    print "Total travellers distance:", D

                if r % show_graph == 0:
                    travelling_route = map_neurons_to_cities(neurons, cities)
                    travelling_route = nodes_to_coordinates(travelling_route, interval_x, interval_y, min_x, min_y)
                    D = calculate_travelers_distance(travelling_route)
                    plot_graph(cities, neurons, country, r, r, D)

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

        travelling_route = map_neurons_to_cities(neurons, cities)
        travelling_route = nodes_to_coordinates(travelling_route, interval_x, interval_y, min_x, min_y)
        D = calculate_travelers_distance(travelling_route)
        plot_graph(cities, neurons, country, num_iterations, "final_plot", D)
        print "Plots have been generated and added to the folder ../plots/" + country
