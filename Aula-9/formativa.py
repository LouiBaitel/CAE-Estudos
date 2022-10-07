'''AVALIAÇÃO FORMATIVA
Certa	loja	de	produtos	de	limpeza	controla	a reposição	de	estoque	por	meio	de	uma	
tabela	na	qual	cada	linha	correspondente	a um	produto	vendido	na	loja.	Para	cada	
produto,	são	armazenados	os	seguintes	dados:
1. nome	do	produto
2. estoque	atual	(em	unidades)
3. estoque	mínimo	(em	unidades)
4. quantidade	mínima	de	compra 

Periodicamente,	o	lojista	analisa	a	tabela	e	gera	uma	lista	com	a	quantidade	a	ser	
comprada	para	cada	produto'''



produto = [
           ["Detergente", 100, 500, 200],\
           ["Alcool", 500, 400, 100],\
           ['Sabão', 200, 500, 400],\
           ['Esponja', 400, 600, 500],\
           ['Alvejante', 700, 500, 300]\
          ]

for p in produto:
   if (p[1] < p [2]): #verifica se se estoque_atual < estoque_minimo
        compra = p [2] - p[1]
        if compra < p [3]: #verifica se a ompra < compra_minima
            compra = p [3]
   else:
        compra = 0
   print (p [0], ': ', compra)