import math

def X (a,b):
    y = abs (math.sqrt (a**2+b**2))
    return y

def Omega (a,b):
    x = X (a,b)
    numerador = math.tan(x)**(1/3)
    #numerador = math.pow (math.tan(x), 1/3)
    denominador = 2*math.pi
    w = numerador/denominador
    return w

#inicio do programa
    
ladoa = float (input ('Medida cateto a: '))
ladob = float (input ('Medida cateto a: '))

omeg = Omega (ladoa, ladob)
omegArre = round (omeg, 2)
print ('O vlaor de omega é', omegArre)