import numpy as np

def shuffle_data(X, y, seed=None):
   
    if seed is not None:
        np.random.seed(seed)

    indices = np.random.permutation(len(X))

    X_shuffled = X[indices]
    y_shuffled = y[indices]

    return X_shuffled, y_shuffled