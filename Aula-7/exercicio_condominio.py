'''
Considere um condomÃ­nio de 4 torres de 10 andares identificados por A, B, C e D,
conforme ilustrado abaixo. Considere ainda que cada andar possui 8 apartamentos,
conforme a planta mostrada abaixo. Escreva um programa em Python baseado em
matrizes para armazenar a informaÃ§Ã£o sobre o preÃ§o de cada apartamento do
condomÃ­nio e realizar as seguintes consultas para encontrar apartamentos Ã  venda

PreÃ§o 0 (zero)=> apartamento nÃ£o estÃ¡ a venda
'''

import numpy as np

Torre = np.array ([[10,30,0,0], \
        [0,0,50,60], \
        [50,0,50,60], \
        [0,70,50,60], \
        [100,0,50,60]])

for a in range (Torre.size [0]): #andar - linha
    for ap in range ((Torre.size [1])): #apartamento - coluna
        if Torre [a,ap] !=0:
            print ("A Venda", a+1, 'o. andar apartamento', ap+1)