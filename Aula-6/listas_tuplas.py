def calculoDesc (p, d):
    valor  = p * (100 - d)/100
    return valor



#lista         0       1           2         3
produto = ['mouse', 'teclado', 'monitor', 'gabinete']
preco =   [14.9,    29.9,         99.9,      250]
quantidade = []
novopreco = []
desconto = []

'''pos = int (input ('Qual é a posição do produto que você deseja? '))
print ('O produto e ', produto [pos-1])'''

#saber quais produtos tem valor maior do que R$ 50,00
#varrer a lista
'''for i in range (0, len(produto), 1): 
    if preco [i] > 50:
        print (produto[i])'''

#ler as quantidades de cada produto no estoque
#for in in range (len(produto)):
i = 0     
while i < len(produto):
    quant = int(input("Qual a quantidade de "+produto[i]+' ?'))
    quantidade.append (quant)
    i = i + 1
    
print (produto)
print (quantidade)

#soma da quantidade de produtos no estoque
somaProd = 0
for i in range (len(produto)):
    somaProd = somaProd + quantidade [i]
    
print ('O Total de produtos no estoque e ', somaProd)

#ler os valores de desconto
for i in range (len(produto)):
    desconto.append (float(input("Qual o desconto do "+produto[i]+' ?')))
    
for i in range (len(produto)):
    novo = calculoDesc (preco [i], desconto [i])
    novopreco.append (novo)
print (novopreco)
  
prod = input ('Qual o prouto deseja comprar? ')
if prod in produto:   #verfifica se o elemento existe na lista
  print ('Existe prouto no estoque!')
else:
  print ('Este produto não está disponível no estoque!')