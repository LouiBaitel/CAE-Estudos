import math 

valor = input('Qual o valor do raio? ')
raio = float (valor)
#raio = float (input('Qual o valor do raio? '))

perimetro = 2 * math.pi * raio
area = math.pi * raio ** 2

print(perimetro)


print ('Área do círculo = ', round (area,2)) #arrendonda em 2 casas
#mesmo resultado de impressão
print ('Área do círculo = ' + str (area))

print (math.trunc (area)) #deixa somente a parte inteira do número
print (math.floor (area)) #arrendonda para baixo
print (math.ceil (area))  #arrendonda para baixo