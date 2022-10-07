#Exercício 2
import matplotlib.pyplot as plt
import numpy as np

delta = 0.01
inf = delta
sup = 1.0 + delta

eixo_x = np.arange(inf, sup, delta)

eixo_y = (1/np.sin(eixo_x)) - np.sqrt(eixo_x * (1-eixo_x))


plt.plot(eixo_x, eixo_y)
plt.show()
