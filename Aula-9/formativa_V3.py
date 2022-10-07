#UTILIZANDO ARRAY
import numpy as np

produto = np.array ([
                    ["Detergente", 100, 500, 200],\
                    ["Alcool", 500, 400, 100],\
                    ['Sabão', 200, 500, 400],\
                    ['Esponja', 400, 600, 500],\
                    ['Alvejante', 700, 500, 300]\
                  ])

for i in range (produto.shape [0]):
   if (int (produto[i,1]) < int (produto [i,2])):#verifica se se estoque_atual < estoque_minimo
        compra = int (produto [i,2]) - int (produto[i,1])
        if compra < int (produto [i,3]): #verifica se a ompra < compra_minima
            compra = produto [i,3]
   else:
        compra = 0
   print (produto [i,0], ': ', compra)