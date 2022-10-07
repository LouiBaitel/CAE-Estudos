palavras = [ ] # lista inicialmente vazia

n = int( input( "Quantas palavras? " ) )

for i in range(n):
    p = input( "Digite a palavra " + str(i + 1) + " : " )
    palavras.append( p ) # insere palavra na lista

palavras.sort ()
print (palavras)