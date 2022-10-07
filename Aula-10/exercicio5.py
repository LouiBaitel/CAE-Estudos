#EXRCICIO 5- AULA 10
import math
import numpy as np
import matplotlib.pyplot as plt

def freq(x):
  y = math.sqrt(2 * math.pi) * math.exp(-(x**2/2))
  return y

X = np.linspace(-10, 10, 2001)
Y = []
for x in X:
  Y.append(freq(x))

plt.plot(X,Y)
plt.show()
