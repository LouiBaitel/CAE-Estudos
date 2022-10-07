#AREA DO TRIANGULO - FORMULA DE HERON
import math

def Heron (a,b,c):
    
    semip = (a+b+c)/2
    A = math.sqrt (semip*(semip-a)*(semip-b)*(semip-c))
    return A

#INICIO DO PROGRAMA
l1 = float (input ("Medida lado 1 do triangulo: "))
l2 = float (input ("Medida lado 2 do triangulo: "))
l3 = float (input ("Medida lado 3 do triangulo: "))

area = Heron (l1,l2,l3)

print ('A area do triangulo e:', round (area,2))