import urllib2
import math
import numpy as np

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

coordinates = get_nodes("Western-Sahara")

def get_nodes_normalized(city_list):
	"The function return a normalized vector of city-coordinates"
	return


def euclidean_distance(start,end):
	"Calculates euclidean distance from two coordinates on the form (a,b)"
	return np.linalg.norm(np.array(start) - np.array(end))

def calc_distance(x1,y1,x2,y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def gen_dist_matrix(coordinates):
    return [[calc_distance(x1,y1,x2,y2) for (x2,y2) in coordinates] for (x1,y1) in coordinates]
