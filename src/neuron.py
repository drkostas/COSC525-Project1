import numpy as np


class Neuron:
    # ACT_FUNCTION, NUM_INPUTS, LEARNING_RATE, [INIT_WEIGHTS]

    def __init__(self, activation: str, num_inputs: int, lr: float, weights: np.ndarray = None):
        # Initializes all input vars
        self.activation = activation
        self.num_inputs = num_inputs
        self.lr = lr
        if weights is None:
            self.weights = (np.random.rand(self.num_inputs) - .5) * 2
        else:
            self.weights = weights
        # Initialize all other object vars
        self.output = None
        self.inputs = None
        self.net = None
        self.partial_der = None

    # Uses the saved net value and activation function to return the output of the node
    def activate(self):
        if self.activation == "linear":
            self.output = self.net
        elif self.activation == "sigmoid":
            self.output = 1 / (1 + np.exp(-self.net))
        return self.output

    # Receives a vector of inputs and determines the nodes output using
    # the stored weights and the activation function
    def calculate(self, inputs):
        self.inputs = inputs
        self.net = np.sum(inputs * self.weights)
        return self.activate()

    # Returns the derivative of the activation function using the previously calculated output.
    def activation_derivative(self):
        if self.activation == "linear":
            return 1
        elif self.activation == "sigmoid":
            return self.output * (1 - self.output)

    # Calculates and saves the partial derivative with respect to the weights
    def derivative(self, delta):
        self.partial_der = self.weights * delta

    # Calculates the new delta*w and calls upon the derivative function
    def calc_partial_derivative(self, deltaw_1):
        delta = np.sum(deltaw_1) * self.activation_derivative()
        self.derivative(delta)
        return delta * self.weights

    # Updates the nodes weights using the saved partial derivatives and learning rate.
    def update_weights(self):
        self.weights = self.weights - self.lr * self.partial_der
