'''Exercícios Complementares Listas e Tuplas
Exercício 6
Em uma loja de informática, tem-se uma relação de produtos/preços/quantidade em estoque.
Crie um programa que inicializa três listas diretamente (ou seja, não precisa ler do usuário): 
a primeira contendo os nomes dos produtos,
a segunda contendo os preços de venda e 
a terceira contendo as quantidades em estoque. 
Depois, deve-se ler do usuário o nome de um produto desejado. 
Caso o produto esteja cadastrado, o programa deve mostrar quantas unidades dele restam em estoque,
bem como o preço unitário. 
Caso contrário, deve-se mostrar mensagem de erro
.
'''

produto = ['mouse','teclado','monitor','gabinete']
preco   = [14.90,   29.90,   399.90,    250.00]
quant   = [100,     150,    20,           35]

compra = input("Qual produdo deseja comprar? ")



#verifica se o produto lido existe na lista
if compra in produto:
    pos = produto.index (compra)
    print ("Existem", quant [pos], compra, "a um valor de R$", preco[pos], 'aunidade')
    
else:
    print ('Produto não cadastrado!')
