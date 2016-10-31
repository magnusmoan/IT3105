from random import random
from utils import *
from graph_generator import plot_graph
import math

country = "Western-Sahara"
cities = normalize_nodes(country)
neurons = []
num_iterations = 1000
K = len(cities * 2)
N = len(cities)

#   Decay-specific parametres
radius = 5
learning_rate = 10.0
delta_learning = 0.001
delta_radius = learning_rate / num_iterations
exponential_rate = 5.0

def find_closest_neuron(neurons, i):
	""" Returns index j of the neuron closest to city i """
	dist_list = [euclidean_distance(neurons[j],cities[i]) for j in range(K)]
	return dist_list.index(min(dist_list))

def find_neighbours(neurons, j):
	""" Returns a list of tuples (indices of neighbours, distance) """
	return [ (k % K, euclidean_distance(neurons[j],neurons[k % K])) for k in range(j - int(math.floor(radius)), j + int(math.floor(radius)))]

def update_weights(neurons, i):
	""" The function finds the closest neuron j to city i, and its 
	neighborhood, and updates the neuron positions """
	
	closest_neuron = find_closest_neuron(neurons, i)
	neighbourhood = find_neighbours(neurons, closest_neuron)

	for (j, dist) in neighbourhood:
		theta = learning_rate * (radius - abs(closest_neuron - j))/radius
		neurons[j][0] += theta * (cities[i][0] - neurons[j][0])
		neurons[j][1] += theta * (cities[i][1] - neurons[j][1])

def calculate_travelers_distance(neurons):
	bridge = euclidean_distance(neurons[0],neurons[-1])
	return sum([euclidean_distance(neurons[j], neurons[j+1]) for j in range(K - 1)]) + bridge

def calculate_error_distance(neurons):
	return sum([euclidean_distance(neurons[find_closest_neuron[i]], cities[i]) for i in range(N)])

def run():

	neurons = [[random(),random()] for _ in range(K)]

	decay_learning = linear(delta_learning)
	decay_radius = linear(delta_radius)

	global learning_rate
	global radius

	plot_graph(cities, neurons, "", 2)
	
	for r in xrange(num_iterations):
		
		for i in xrange(N):
			update_weights(neurons,i)
		
		print neurons
		break
	    		
		learning_rate = decay_learning(learning_rate)
		radius = decay_radius(radius)
	
#	plot_graph(cities, neurons, "", 2)

run()
