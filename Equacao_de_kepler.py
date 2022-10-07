'''Equação Radial de Kepler'''

#para utilizar as funções da Biblioteca Matemática
import math

# x variando de 0.1 a 1, com incremento de 0.1

x = 0.1

tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.2
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.3
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.4
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.5
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.6
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.7
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.8
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=0.9
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)

x = x+0.1 # x=1
tx = math.asin(math.sqrt(x)) - math.sqrt(x*(1-x))
print (tx)
