'''Exercícios Complementares Listas e Tuplas
Exercício 2
Elabore uma app em Python para gerar e imprimir duas listas, 
uma com os valores pares e outra com os valores ímpares de 0 a 100
'''
par = []
impar = []

for i in range (0,101,1): #gera os valores dea 0 A 100
    resto = i%2 #calcula o resto da divisao
    if resto == 0:
        resto = i%2 #calcula o resto da divisao
    if resto == 0:
        par.append (i)
    else:
        impar.append (i)
        
    
print ("Numeros pares = ", par)
print ("Numeros impares = ", impar)