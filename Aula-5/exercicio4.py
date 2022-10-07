'''Exercícios Complementares Listas e Tuplas
Exercício 4
Elabore uma app em Python para ler duas listas de 10 valores reais 
digitados pelo usuário. 
Em seguida, gere uma terceira lista com a soma dos valores de índice opostos
(Ex. índice Lista_1[0] + Lista_2[9], ...). 
Ao final, imprima as três listas.
'''
A = []
B = []
SomaAB = []


#Leitura dos valores da lista A 
for i in range (10): #for i in range (0,N,1):
    valor = float(input ("A"+ str (i+1) +" = "))
    A.append (valor)
    
#Leitura dos valores da lista A 
for i in range (10): 
    B.append (float(input ("B"+ str (i+1) +" = ")))

#gerar a lista SomaAB
for i in range (10):  
    AB = A[i] + B [9-i]
    SomaAB.append (AB)
    

print (A)
print (B)
print (SomaAB)
