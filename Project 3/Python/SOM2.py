from random import random
from utils import *
from graph_generator import plot_graph
import math

country = "Western-Sahara"
cities = get_nodes_normalized(country)
neurons = []
num_iterations = 1000
K = len(cities * 2)
N = len(cities)

#   Decay-specific parametres
radius = 5
learning_rate = 10.0
delta_learning_rate = 0.001
delta_radius = learning_rate / num_iterations
exponential_rate = 5.0

def init():
	""" Generates random neurons, computes weights	"""
	neurons = [(random(), random()) for _ in range(K)]

def find_closest_neuron(i):
	""" Returns index j of the neuron closest to city i """
	dist_list = [euclidean_distance(neurons[j],cities[i]) for j in range(K)]
	return dist_list.indexof(min(dist_list))

def find_neighbours(j):
	""" Returns a list of tuples (indices of neighbours, distance) """
	return [ (k, euclidean_distance(neuron[i],neuron[k % K])) for k in range(j - radius, j + radius)]

def static(rate):
	return rate

def linear(rate):
	return rate - 0.001

def exponential(rate):
	return math.exp(-rate/exponential_rate)
	
def decay(decay_function, rate):
	return decay_function(rate)

def update_weights(i):
	""" The function finds the closest neuron j to city i, and its 
	neighborhood, and updates the neuron positions """
	
	closest_neuron = find_closest_neuron(i)
	neighbourhood = find_neighbours(closest_neuron)

	for (j, dist) in neighbourhood:
		theta = learning_rate * (radius - dist) / radius
		neurons[j][0] += theta * (cities[i][0] - neurons[j][0])
		neurons[j][1] += theta * (cities[i][1] - neurons[j][1])

def calculate_travelers_distance():
	bridge = euclidean_distance(neurons[0],neurons[-1])
	return sum([euclidean_distance(neurons[j], neurons[j+1]) for j in range(K - 1)]) + bridge

def calculate_error_distance():
	return sum([euclidean_distance(neurons[find_closest_neuron[i]], cities[i]) for i in range(N)])

def run():
	init()

	for r in xrange(num_iterations):
		
		for i in xrange(N):
			update_weights(i)

		learning_rate = decay(linear, learning_rate)
		radius = decay(linear, radius)
		

run()
