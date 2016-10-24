import urllib2

country_mapping = {
	    "Western-Sahara" : "wi29.tsp", 
	    "Djibouti" : "dj38.tsp", 
	    "Qatar" : "qa194.tsp",
	    "Urugay" : "uy734.tsp"	    
	    }

#   Takes country_id as input and fetches the coordinates from the web-page
def get_nodes(country_id):
	nodes = []
	data = urllib2.urlopen("http://www.math.uwaterloo.ca/tsp/world/" + country_id)
	for line in data:
		line_list = line.split(" ")
		if line_list[0].isdigit():
			latitude, longitude = line_list[1], line_list[2][:-2]
			nodes.append([latitude, longitude])
	return nodes




