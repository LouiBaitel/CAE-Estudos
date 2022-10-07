import math

def P (x,y,z):
    return ((x+y+z)/2)

def Heron (a,b,c):
    semip = P (a,b,c)
    A = math.sqrt (semip*(semip-a)*(semip-b)*(semip-c))
    return A

#INICIO DO PROGRAMA
l1 = float (input ("Medida lado 1 do triangulo: "))
l2 = float (input ("Medida lado 2 do triangulo: "))
l3 = float (input ("Medida lado 3 do triangulo: "))

area = Heron (l1,l2,l3)

print ('A area do triangulo e:', round (area,2))