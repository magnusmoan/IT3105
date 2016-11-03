import matplotlib.pyplot as plt
import os

# Input: Normalized coordinate lists representing cities and neurons.
def plot_graph(city_nodes, neurons, country, iteration_no, plot_name, total_distance):

    fig, ax = plt.subplots()
    fig.canvas.set_window_title("IT3105: Project 3")
    
    city_line = plt.scatter(*zip(*city_nodes), c='#00ABFF', label='Cities')

    # Plots all neurons
    plt.plot([neurons[-1][0], neurons[0][0]], [neurons[-1][1], neurons[0][1]], color='#FF5500')
    plt.plot(*zip(*neurons), c='#FF5500', marker='o', mew=0.0, label='Neurons', ms=5)

    plt.axis([-0.1,1.1,-0.1,1.1])
    plt.legend(bbox_to_anchor=(1.1, 1.1))
    plt.title("SOM solving TSP for " + country + ".\nIteration number: " + str(iteration_no) +
            "\nTotal distance (D): " + '{0:.0f}'.format(total_distance))

    if plot_name == "initial_plot":
        try:
            for file in os.listdir("../plots/" + country):
                os.remove("../plots/" + country + "/" + file)
        except OSError:
            pass
    try:
        plt.savefig("../plots/" + country + "/" + str(plot_name))
    except IOError:
        os.mkdir("../plots/" + country)
        plt.savefig("../plots/" + country + "/" + str(plot_name))

    plt.close()
