'''EXERCICIO 1 - SOMA DAS MATRIZES A e '''


A = [] 
B = []
C = [] #soma das matrizes A e B

m = int(input('Quantas linhas em cada matriz? '))
n = int(input('Quantas colunas em cada matriz? '))

#criar a matriz A com valores zero
for l in range (m):
    linha = []    #cria uma linha para colocar as notas da disciplina
    for c in range (n):
        linha.append (0)
    A.append (linha)
    
#leitura dos valores da matriz A
for l in range (m):
    for c in range (n):
        A [l][c] = float(input ('A'+str(l+1)+str(c+1)+': '))

#criar a matriz B com leitura de valores 
for l in range (m):
    linha = []    #cria uma linha os valores da coluna
    for c in range (n):
        linha.append (float(input ('B'+str(l)+str(c)+': ')))
    B.append (linha)

#criar a matriz C com as soma de cada elemento de A e B 
for l in range (m):
    linha = []   
    for c in range (n):
        c = A [l][c] + B[l][c]
        linha.append (c)
    C.append (linha)


#impressao da matriz
for l in range (len(A)):
    print (A[l])

print ('********************************')
#impressão das matrizes
print ('    A + B = C ')

for l in range (m):
    print (A [l], '  ', B [l], '  = ', C [l])