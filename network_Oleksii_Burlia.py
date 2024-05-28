import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):  #activation function (here: leaky_relu)
        return max(x * .1, x)

    def __call__(self,
                 xs):  #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
        # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b)


class NeuralNetwork:
    def __init__(self, biases, weights):
        self.layers = []

        self.layers.append([Neuron(4, bias=biases[0][i], weights=weights[0][i]) for i in range(4)])
        self.layers.append([Neuron(4, bias=biases[1][i], weights=weights[1][i]) for i in range(4)])
        self.layers.append([Neuron(4, bias=biases[2][0], weights=weights[2][0])])

    def activate(self, inputs):
        input_data = inputs
        for layer in self.layers:
            output_data = []
            for neuron in layer:
                output_data.append(neuron(input_data))
            input_data = np.array(output_data)
        return input_data

    def visualize(self):
        n_layers = len(self.layers)
        n_neurons = [len(layer) for layer in self.layers]

        fig, ax = plt.subplots()

        ax.set_xlim(-0.5, n_layers - 0.5)
        ax.set_ylim(-0.5, max(n_neurons) - 0.5)
        ax.set_aspect('equal')

        ax.axis('off')

        for i, layer in enumerate(self.layers):
            for j, neuron in enumerate(layer):
                circle = plt.Circle((i, j), 0.05, color='blue', zorder=10)
                ax.add_artist(circle)

                if i > 0:
                    for k in range(len(self.layers[i - 1])):
                        line = plt.Line2D([i - 1, i], [k, j], color='gray', zorder=0)

        plt.title("Neural Network Architecture Visualization")
        plt.savefig("neural_network_visualization.png")


test_weights = [[
    [1.2, 0.2, 3.1],
    [1.5, 0.1, 1.2],
    [1.6, 8.01, 1.1],
    [5.1, 0.4, 0.01]
], [[2.1, 3.2, 4.2, 7.0],
    [0.01, 0.2, 3.2, 1.7],
    [0.8, 0.6, 0.2, 3.2],
    [1.6, 0.5, 2.2, 1.1]
], [[2.0, 1.7, 2.4, 4.1]]]

test_input_data = [1.2, 3.2, 0.1]
test_biases = [[
    1.1, 2.4, 0.01, 2.3
], [
    2.1, 2.2, 2.3, 1.3
], [-1.1]]

network = NeuralNetwork(test_biases, test_weights)
result = network.activate(test_input_data)
print(result)
network.visualize()
