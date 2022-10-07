import math

def Fx (x0, x, L, k):
    valor = -k*(x-x0)
    y = L/ (math.exp (valor))
    return y

#x = -6
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)

#x = -4
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)

#x = -2
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)

#x = 0
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)

#x = 2
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)

#x = 4
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)

#x = 6
valor = float (input ('Digite o valor de x: '))
res = Fx (0, valor, 1,1)
print (res)
