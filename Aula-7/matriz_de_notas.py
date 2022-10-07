'''EXEMPLO MATRIZ NOTAS
LINHAS => disciplinas
COLUNAS => notas '''

NOTAS = [[10.0, 9.0, 8.5], [5.4, 7.8, 6.3], [6.8, 7.5, 3.4], [7.0,8.0,9.0]]

for i in range (len(NOTAS)): 
    print (NOTAS[i]) #imprime linha por linha da matriz

disciplinas = len(NOTAS) #numero de disciplinas é numero de linhas  
colunas = len (NOTAS[0]) #numero de notas por disciplina é numero de colunas 

#corrigir a nota 3.4 após a recuperação linha 2 coluna 2
NOTAS [2][2] = 9.5

#corrigir a nota 5.4 linha 1 e na coluna 0
NOTAS [1][0] = 8.0

for i in range (len(NOTAS)): 
    print (NOTAS[i]) #imprime linha por linha da matriz