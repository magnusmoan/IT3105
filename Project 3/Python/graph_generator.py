import matplotlib.pyplot as plt

# Input: Normalized coordinate lists representing cities and neurons.
def plot_graph(city_nodes, neurons, country, iterationNo=0):

    plt.figure().canvas.set_window_title("IT3105: Project 3")
    # Plots all cities
    city_line = plt.scatter(*zip(*city_nodes), c='#00ABFF', label='Cities')

    # Plots all neurons
    plt.plot([neurons[-1][0], neurons[0][0]], [neurons[-1][1], neurons[0][1]], color='#FF5500')
    neurons_line = plt.plot(*zip(*neurons), c='#FF5500', marker='o', mew=0.0, label='Neurons', ms=5)

    plt.axis([-0.1,1.1,-0.1,1.1])
    plt.legend(bbox_to_anchor=(1.1, 1.1))
    plt.title("SOM solving TSP for " + country + ".\nIteration number: " + str(iterationNo))

    plt.show()
