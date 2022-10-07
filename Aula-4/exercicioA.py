import math

def fx (x):
    
    y = math.cos (x) / math.sqrt (1-x)
    return y


#inicio do programa
a = float(input ('Entre com o valor do angulo em radianos (entrte 0 e 1): '))

Fx = fx (a)
print ('f(',a,')=', Fx)
