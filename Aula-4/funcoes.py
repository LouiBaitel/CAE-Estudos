def somar (a, b):
    x = a + b
    return x

#INICIO DO PROGRAMA
z = int(input ('Valor a: '))
w = int(input ('Valor b: '))

y = somar (z,w)

print (y)

y = somar( 10, 15 )
print( y )

print( somar( 8, 2 ) )

j = somar (z,w) + y + somar (y, 23)
print (j)
