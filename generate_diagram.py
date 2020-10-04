import collections
from bigfloat import mul, sub, precision
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def logistic_map(x0, r, iterations, length):
    x = collections.deque([x0], maxlen=length)
    for i in range(iterations):
        x.append(r*x[-1]*(1-x[-1]))
    return x


fig, ax = plt.subplots()

R = np.linspace(0, 10, 101)
N = 100
x = 0.000001
for r in tqdm(R):
    X = logistic_map(x, r, 5*N, N)
    ax.scatter([r]*N, X, marker='.', color='red', linewidth=0.01)
    
fig.savefig('fig.png', dpi=300)
