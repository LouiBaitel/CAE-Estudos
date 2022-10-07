'''EXEMPLO - FUNÇÃO DE SOMA DE  VALORES DE UMA MATRIZ
NUMPY
'''
import numpy as np

A = np.array ([[2,2,2],[4,4,4], [5,5,5], [6,6,6]])
print (A)

somaValores = np.sum(A)

print ('A soma dos valores é ', somaValores)
print ('A media dos valores é ', somaValores/A.size)

print ("Soma dos valores das Colunas")
print (np.sum(A, axis=0))

print ("Soma dos valores das Linhas")
print (np.sum(A, axis=1))

