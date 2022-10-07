#RESOLUÇÃO COM ARRAY

import numpy as np

america = np.array ([\
           ['Brasil', 212559426],\
           ['Colombia', 50882891],\
           ['Argentina', 45195774],\
           ['Peru', 33050325],\
           ['Venezuela', 28435940],\
           ['Chile', 19116201],\
           ['Equador', 1764054],\
           ['Bolivia', 11673021],\
           ['Paraguai', 7132538],\
           ['Uruguai', 3473730],\
           ['Guiana', 786552],\
           ['Suriname', 588552]\
])


populacaoAM = 0    #somar as poulações de cada pais

for p in range (america.shape [0]): #linhas que são os paises
    print (america[p,0], 'populacao = ', int (america[p,1]))
    populacaoAM = populacaoAM + int (america[p,1])

print ('A poulacao total da America Latina e ', populacaoAM )