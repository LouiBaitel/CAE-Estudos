#EXRCICIO 5- AULA 10
import math
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-10, 10, 2001)
Y = np.sqrt(2 * math.pi) * np.exp(-(X**2/2))

plt.plot(X,Y)
plt.show()

