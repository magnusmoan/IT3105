from random import random
from utils import *
from graph_generator import plot_graph
import math

country = "Western-Sahara"
cities = get_nodes_normalized(country)
neurons = []
radius = 0.2
learning_rate = 10.0
delta_radius = 0.0001
delta_learning_rate = 0.001
weight = []
dist = []
K = N = len(cities)
num_iterations = 1000

def init():
	""" Generates random neurons, computes weights	"""
	for i in xrange(N):
		
		#   TODO: Implement static numpy arrays
		weight.append([])
		dist.append([])

		for j in xrange(K):

			#   TODO: Implement static numpy arrays
			dist[i].append([])
			weight[i].append([0,0])
			
                        """ Her er det noe som skurrer for meg: Listen neurons inneholder tupler av typen (x,y), hva skal vi da med weights? 
                            Holder det ikke å bruke neuronslisten som weights? """
			neurons.append([random(), random()])
			weight[i][j][0] = cities[i][0] - neurons[j][0]
			weight[i][j][1] = cities[i][1] - neurons[j][1]
			dist[i][j] = euclidean_distance(cities[i], (neurons[j][0],neurons[j][1]))

def find_closest_neuron(i):
	""" Returns index j of the neuron closest to city i """
	return dist[i].index(min(dist[i])) # Changed max to min, correct?

def find_neighbours(j):
	""" Returns a list of tuples of the form (index of neuron, distance 
	from neuron j). The returned list includes the neuron j itself """
	
	neighbours = []
        neuron_j = neurons[j]

	for i in xrange(K):

		dist_ij = euclidean_distance(neurons[i], neuron_j)

		if (dist_ij <= radius):
			neighbours.append((i, dist_ij))

	return neighbours

def update_weights(i):
	""" The function fins the closest neuron j to city i, and its 
	neighborhood, and updates the weight vectors, distance matrix
	and neuron positions """
	
	closest_neuron = find_closest_neuron(i)
	neighbourhood = find_neighbours(closest_neuron)

	for (j, dist) in neighbourhood:
		
		#   TODO: Implement different learning functions
		theta = learning_rate * (radius - dist) / radius
		
		delta_x = theta * (cities[i][0] - weight[i][j][0])
		delta_y = theta * (cities[i][1] - weight[i][j][1])
		
		neurons[j][0] += delta_x
		neurons[j][1] += delta_y

		for k in xrange(N):
			weight[k][j][0] += delta_x
			weight[k][j][1] += delta_y
			dist[k][j] = euclidean_distance( (weight[k][j][0], weight[k][j][1]), cities[k])

def calculate_distance():
	""" The function returns the total distance of the neurons """
	return

def run():
	init()

	#   TODO: Should be user-specified
	print_frequency = 10
        print cities
        plot_graph(cities, neurons, country)
        return

	for r in xrange(num_iterations):
		
		for i in xrange(N):
			update_weights(i)

		learning_rate -= delta_learning_rate
		radius -= delta_radius

                plot_graph
	
		if (r % print_frequency == 0):
			print "Distance",calculate_distance(),"in round",r

run()
