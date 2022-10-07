inicio = int(input('Qual o valor inicial da lista? '))
fim = int(input('Qual o valor final da lista? '))

numeros = [] #lista sem valores
print (numeros)

for i in range (inicio, fim+1,1): #gera os valores da lista
    numeros.append (i)
    
print (numeros)

#somar os valores da lista
soma = 0 
for i in range (len(numeros)):
    soma = soma + numeros [i]
    
print ("A soma dos valores no intervalo ", soma)