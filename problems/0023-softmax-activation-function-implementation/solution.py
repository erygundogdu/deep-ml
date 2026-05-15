import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores = np.array(scores)
    scores = scores -max(scores)
    exp = np.exp(scores)
    sm = np.sum(exp) + 1e-8
    result = exp / sm
    return result
    pass