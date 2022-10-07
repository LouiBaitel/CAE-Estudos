#Versão 2
produto = [
           ["Detergente", 100, 500, 200],\
           ["Alcool", 500, 400, 100],\
           ['Sabão', 200, 500, 400],\
           ['Esponja', 400, 600, 500],\
           ['Alvejante', 700, 500, 300]\
          ]

for i in range (len (produto)):
    if (produto[i][1] < produto [i][2]):#verifica se se estoque_atual < estoque_minimo
        compra = produto[i][2] - produto[i][1]
        if compra < produto [i][3]: #verifica se a ompra < compra_minima
            compra = produto [i][3]
    else:
        compra = 0
    print (produto [i][0], ': ', compra)


    