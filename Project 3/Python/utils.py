import urllib2
import numpy as np


def get_nodes(country_id):
	"Takes country_id as input and gets the coordinates from the web-page"
	nodes = []
	data = urllib2.urlopen("http://www.math.uwaterloo.ca/tsp/world/" + country_id)
	for line in data:
		line_list = line.split(" ")
		if line_list[0].isdigit():
			latitude, longitude = float(line_list[1]), float(line_list[2][:-2])
			nodes.append([latitude, longitude])
	return nodes


def get_nodes_normalized(city_list):
	"The function return a normalized vector of city-coordinates"
	return


def euclidean_distance(start,end):
	"Calculates euclidean distance from two coordinates on the form (a,b)"
	return np.linalg.norm(np.array(start) - np.array(end))


