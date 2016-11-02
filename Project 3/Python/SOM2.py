from random import random, choice
from utils import *
from graph_generator import plot_graph, update_graph, show_final_graph
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
	dist_list = [euclidean_distance(neurons[j],city) for j in range(no_of_neurons)]
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
	return sum([euclidean_distance(neurons[j], neurons[j+1]) for j in range(no_of_neurons - 1)]) + bridge

def run(parameters):

	decay_learning = parameters['l_r']
	decay_radius = parameters['n_r']

        learning_rate0 = learning_rate = parameters['init_l_r']
        radius0 = radius = parameters['init_radius']

        num_iterations = parameters['n']
        country = parameters['country']
        cities = normalize_nodes(country)
        no_of_neurons = len(cities) * 3
	neurons = init_neurons(no_of_neurons) 
        graph = plot_graph(cities, neurons, country, num_iterations)

	for r in xrange(num_iterations):
                if r % 200 == 0:
                    graph = update_graph(neurons, country, graph)
                print r
                radius = int(math.floor(radius))
		update_weights(neurons, choice(cities), learning_rate, radius, no_of_neurons)
	    		
		learning_rate = decay_learning(learning_rate0, r)
                radius = decay_radius(radius0, r)

	


