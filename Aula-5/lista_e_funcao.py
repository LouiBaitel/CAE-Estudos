#LISTAS - CALCULAR g(x) para um valor de x

import math 

def g(x):
    res = math.log2(x) + math.pi**3/2*math.exp(x)
    return res

#inicio do programa
X = []
Gx = []
n = int(input("Quantos valores de x? "))    

#Leitura dos valores de x
for i in range (n):
  valor = float(input ('Entre com o valor de x: '))
  X.append (valor)
  #X.append (float(input ('Entre com o valor de x: ')))

print (X)

for i in range (n):
  y = g(X[i])  
  Gx.append (y)
  #Gx.append (g(X[i]) )

