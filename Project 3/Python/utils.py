import matplotlib.pyplot as plt
from time import time
import urllib2
import math
import numpy as np
from graph_generator import plot_graph

country_mapping = {
	    "Western-Sahara" : "wi29.tsp", 
	    "Djibouti" : "dj38.tsp", 
	    "Qatar" : "qa194.tsp",
	    "Uruguay" : "uy734.tsp",
            "China" : "ch71009.tsp"
	    }


def get_nodes(country_id):
	"Takes country_id as input and gets the coordinates from the web-page"
	nodes = []
        internet = True

        if internet:
            data = urllib2.urlopen("http://www.math.uwaterloo.ca/tsp/world/" + country_mapping[country_id])
        else:
            data = open("./../data/" + country_mapping[country_id], 'r')
	for line in data:
		line_list = line.split(" ")
		if line_list[0].isdigit():
			latitude, longitude = line_list[1], line_list[2][:-2]
			nodes.append([float(latitude), float(longitude)])
        data.close()
	return nodes


def normalize_nodes(country):
        city_list = get_nodes(country)
	"The function return a normalized vector of city-coordinates"
        # TODO: Bytt ut python lister med numpy arrays
        max_x = max(city_list, key=lambda x: x[0])[0]
        max_y = max(city_list, key=lambda y: y[1])[1]
        min_x = min(city_list, key=lambda x: x[0])[0]
        min_y = min(city_list, key=lambda y: y[1])[1]

        interval_x = max_x - min_x
        interval_y = max_y - min_y

        nodes_normalized = []
        
        for (x,y) in city_list:
            x_norm = (x - min_x) / interval_x
            y_norm = (y - min_y) / interval_y

            nodes_normalized.append([x_norm, y_norm])

	return np.array(nodes_normalized)

def euclidean_distance(start,end):
    return math.sqrt( (end[0] - start[0])**2 + (end[1] - start[1])**2 )


def linear(x, t, delta):
    return x - t*delta

def exponential(lam):
    return lambda x, t: x*math.exp(-t/lam)


def static(rate, t):
    return rate
