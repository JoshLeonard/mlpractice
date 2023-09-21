import numpy as np
import random

def compute_net(w, x):
    result = np.dot(w, x)
    if result < 0:
        return -1
    else:
        return 1

def get_random_weights(weight_counts):
    weights = []
    for i in range(weight_counts):
        weights.append(np.random.normal())
    
    return weights


weights = get_random_weights(3)
print(weights)