'''EXEMPLO MATRIZ NOTAS - LEITURA DE VALORES DO USUÁRIO
Criar uma matriz com zeros antes para iniciar a matriz
LINHAS => disciplinas
COLUNAS => notas '''

NOTAS = [] #matriz com as notas de cada disciplina
quantlinhas = int(input('Quantas disciplinas existem? '))
quantcolunas = int(input('Quantas notas para cada disciplina? '))

#criar a matriz com valores zero
for l in range (quantlinhas):
    linha = []    #cria uma linha para colocar as notas da disciplina
    for c in range (quantcolunas):
        linha.append (0)
    NOTAS.append (linha)
    

#impressao da matriz
for l in range (len(NOTAS)):
    print (NOTAS [l])
