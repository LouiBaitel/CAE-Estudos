import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4],\
         [1, 4, 2, 3])

plt.show()

# Exemplo 1
import matplotlib.pyplot as plt
eixo_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
eixo_y = [10, 8, 6, 9, 12, 15, 13, 16, 14, 18, 12,
15]
plt.plot(eixo_x, eixo_y)
plt.grid()
plt.title("Vendas durante o ano")
plt.xlabel("Mês")
plt.ylabel("Unidades vendidas")
plt.show()
#———————————————————————————

# Exemplo 2
import matplotlib.pyplot as plt
alturas = [160, 170, 162, 175, 183, 155, 165, 172, 164, 181]
barras = [150, 160, 170, 180, 190]
plt.hist(alturas, bins=barras, rwidth=0.4, color='g')
plt.title("Distribuição das pessoas por altura")
plt.xlabel("Altura")
plt.ylabel("Quantidade de pessoas")
plt.show()
#———————————————————————————