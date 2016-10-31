import matplotlib.pyplot as plt
import urllib2
import math
import numpy as np
from graph_generator import plot_graph

country_mapping = {
	    "Western-Sahara" : "wi29.tsp", 
	    "Djibouti" : "dj38.tsp", 
	    "Qatar" : "qa194.tsp",
	    "Urugay" : "uy734.tsp"	    
	    }


def get_nodes(country_id):
	"Takes country_id as input and gets the coordinates from the web-page"
	nodes = []
        internet = False

        if internet:
            data = urllib2.urlopen("http://www.math.uwaterloo.ca/tsp/world/" + country_id)
        else:
            data = open("./../data/" + country_mapping[country_id], 'r')
	for line in data:
		line_list = line.split(" ")
		if line_list[0].isdigit():
			latitude, longitude = line_list[1], line_list[2][:-2]
			nodes.append((float(latitude), float(longitude)))
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

            nodes_normalized.append((x_norm, y_norm))

	return np.array(nodes_normalized)

normalized = normalize_nodes("Western-Sahara")
test_list = [(8.0,9.0), (10.0, 1.0), (0.0, 2.0), (3.0,4.0), (5.0,0.0), (8.6, 10.0)]
print normalized
#normalized1 = get_nodes_normalized(test_list)
#normalized2 = get_nodes_normalized(coordinates)

#plot_graph(normalized2, normalized1, "West-Sahara", iterationNo=10)


def euclidean_distance(start,end):
	"Calculates euclidean distance from two coordinates on the form (a,b)"
	return np.linalg.norm(np.array(start) - np.array(end))

def calc_distance(x1,y1,x2,y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def gen_dist_matrix(coordinates):
    return [[calc_distance(x1,y1,x2,y2) for (x2,y2) in coordinates] for (x1,y1) in coordinates]


