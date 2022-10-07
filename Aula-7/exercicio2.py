'''EXERCICIO 2 - multiplicacao DAS MATRIZES A e B
NUMPY
'''
import numpy as np

linB = int(input('Qual o numero de linhas de B? '))
colB = int(input('Qual o numero de colunas de B? '))

#criar o array (matriz) B
B = np.zeros ((linB,colB))

for l in range (linB):
    for c in range (B.shape [1]):
        B [l,c] = int(input('B'+str(l)+str(c)+': '))
        
linA = A.shape [0]
colB = A.shape [1]

#verificar se as matrizes podem ser multiplicadas
#no colunas A deve ser igual ao no Linhas de B

if colB != linB:
    print ('Não é possível multiplicar as matrizes!')
else:
    C = A.dot(B)
    print (A)
    print (B)
    print (C)
        