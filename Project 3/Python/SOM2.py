from random import random
from utils import *
from graph_generator import plot_graph
from time import time
import math

start = time()
closest = 0
find_neigh = 0
update = 0

def find_closest_neuron(neurons, city):
	""" Returns index j of the neuron closest to city i """
        K = len(neurons)
	dist_list = [euclidean_distance(neurons[j],city) for j in range(K)]
	return dist_list.index(min(dist_list))

def find_neighbours(neurons, j, radius):
	""" Returns a list of tuples (indices of neighbours, distance) """
        K = len(neurons)
        best_matching_unit = neurons[j]
        start = j - int(math.floor(radius))
        end = j + int(math.floor(radius)) + 1
	return [ (k % K, euclidean_distance(best_matching_unit, neurons[k % K])) for k in range(start, end)]

def update_weights(neurons, city, learning_rate, radius):
	""" The function finds the closest neuron j to city i, and its 
	neighborhood, and updates the neuron positions """
        global closest, find_neigh, update
	
        time1 = time()
	closest_neuron = find_closest_neuron(neurons, city)
        closest += time() - time1
        time2 = time()
	neighbourhood = find_neighbours(neurons, closest_neuron, radius)
        find_neigh += time() - time2

        time3 = time() 
	for (j, dist) in neighbourhood:
		discount = learning_rate * math.exp(- dist**2 / (2 * radius**2 ))
		neurons[j][0] += discount * (city[0] - neurons[j][0])
		neurons[j][1] += discount * (city[1] - neurons[j][1])
        update += time() - time3


def calculate_travelers_distance(neurons):
	bridge = euclidean_distance(neurons[0],neurons[-1])
	return sum([euclidean_distance(neurons[j], neurons[j+1]) for j in range(K - 1)]) + bridge

def calculate_error_distance(neurons):
        # "find_closest_city" istedenfor "find_closest_neuron"
        return
	#return sum([euclidean_distance(neurons[find_closest_neuron[i], cities[i]) for i in range(N)])

def run(parameters):
	decay_learning = parameters['l_r']
	decay_radius = parameters['n_r']

        learning_rate = parameters['init_l_r']
        radius = parameters['init_radius']

        num_iterations = parameters['n']
        country = parameters['country']
        cities = normalize_nodes(country)
        N = len(cities)
        K = N*3

	neurons = [[random(),random()] for _ in range(K)]

	plot_graph(cities, neurons, country, 0)
	
	for r in xrange(num_iterations):
		for i in xrange(N):
			update_weights(neurons,cities[i], learning_rate, radius)
	    		
		learning_rate = decay_learning(learning_rate)
		radius = decay_radius(radius)
	
        print "Find neighbor: " + str(find_neigh)
        print "Closest: " + str(closest)
        print "Update: " + str(update)
        plot_graph(cities, neurons, country, num_iterations)


