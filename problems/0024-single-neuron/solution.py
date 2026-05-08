import math
import numpy as np

def single_neuron_model(features: list[list[float]],
                        labels: list[int],
                        weights: list[float],
                        bias: float) -> (list[float], float):


    X = np.array(features)
    y = np.array(labels)
    w = np.array(weights)

    
    z = np.dot(X, w) + bias

    
    y_hat = 1 / (1 + np.exp(-z))

    
    mse = np.mean((y_hat - y) ** 2)

    return y_hat.tolist(), mse