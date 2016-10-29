from utils import *
from random import random

country_mapping = {
	    "Western-Sahara" : "wi29.tsp", 
	    "Djibouti" : "dj38.tsp", 
	    "Qatar" : "qa194.tsp",
	    "Urugay" : "uy734.tsp"	    
	    }

CITIES_ORIGINAL = get_nodes(country_mapping["Western-Sahara"])	#Gets a list of coordinates
CITIES = get_nodes_normalized(CITIES_ORIGINAL) #The list contains an ordered, normalized vector of city coordinates
LEARNING_RATE = 10.0	#Learning rate for updating neuron weights
DELTA = 0.001	#For linear reduction of learning rate
RADIUS = 1.0/10.0 * len(CITIES) #Must implement static, linear and exponential neighborhood radius
MAX_ITER = 100	#Number of rounds


class Neuron:
	"The class defines a neuron-object designed to hold attributes and functinoality of the output layer neurons"
	def __init__(self):
		self.weights = self.init_weights()
	
	def init_weights(self):
		"Generates a random and normalized weight vector from current Neuron to city j"
		weights = []
		for j in xrange(len(CITIES)):
			weights.append([random(),random()])
		return weights

	def update_weight(self, city_j, learning_rate = LEARNING_RATE):
		"Updates weights for a given city j according to its learning rate"
		self.weights[city_j][0] += learning_rate * (CITIES[city_j][0] - self.weights[city_j][0])
		self.weights[city_j][1] += learning_rate * (CITIES[city_j][1] - self.weights[city_j][1])

def find_best_neuron(city_j):
	"For a given city j, the function finds the closest neuron based on their weights"
	return neuron

def find_neighborhood(neuron, radius):
	"For a given neuron i, the function finds the closest neurons based on current neighborhood radius"
	return

def update_neurons(city_j):
	"Updates weight on all relevant neurons, taking into account different learning rates"
	neuron = find_best_neuron(city_j)
	neighboors = find_neighborhood(neuron)
	return
	
def calculate_distance():
	"Calculates total distance on current ring of neurons"
	return

def init_neurons():
	"Initializes a ring of neurons based on the number of cities in current problem"
	return

def run():

	distance = float("inf")

	for training_round in xrange(MAX_ITER):
	    
		for j in CITIES:
			update_neurons(j)

		distance = calculate_distance()


run()
	
