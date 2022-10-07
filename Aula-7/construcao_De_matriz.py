import numpy as np

m = int(input('Quantas linhas a matriz tem? '))
n = int(input('Quantas colunas a matriz tem? '))

A = np.zeros ((m,n))
B = np.zeros ((m,n))


#ler os valores da matriz A 
for l in range (m):
   for c in range (n):
       A[l,c] = float (input ('A'+str(l)+str(c)+': ')) 

#ler os valores da matriz B 
for l in range (m):
   for c in range (n):
       B [l,c] = float (input ('B'+str(l)+str(c)+': ')) 


#soma da matriz A com a B
C = A + B
       
print ('********************************')
#impressão das matrizes
print ('    A + B = C ')

for l in range (m):
    print (A [l], '  ', B [l], '  = ', C [l])