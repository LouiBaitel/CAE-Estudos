import numpy as np

V = np.array([1, 2, 3, 4, 5])
#V = np.array([4.5, 8.0, 6.3, 9.1, 5.7, 7.5, 9.5, 8.6])

media = np.average(V)
n = np.size(V)

Dp = np.sqrt((1/n) * np.sum(np.square(V - media)))

print(Dp)
