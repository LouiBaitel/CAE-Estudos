'''Exercícios Complementares Listas e Tuplas
Exercício 1
Elabore uma app em Python para ler dois valores inteiros, 
sendo o segundo maior que o primeiro, e gere e imprima uma lista 
dos valores no intervalo fechado. 
'''


inicio = int(input('Qual o valor inicial da lista? '))
fim = int(input('Qual o valor final da lista? '))

numeros = [] #lista sem valores
print (numeros)

for i in range (inicio+1, fim,1): #gera os valores da lista
    numeros.append (i)
    
print (numeros)