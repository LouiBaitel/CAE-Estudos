'''Equação de Prony

Programa que calcule hf em um tubo com fluido
em movimento para quaisquer valores de L, D, V, a, b '''


#Entrada de dados
L = float (input('Entre com o comprimento do tubo: '))
D = float (input('Entre com o diâmetro do tubo: '))
V = float (input('Entre com a velocidade do fluido: '))
a = float (input('Entre com o fator impírico para ponderar fricção a: '))
b = float (input('Entre com o fator impírico para ponderar fricção b: '))

#Calculo de hf => Head loss (energia dissipada) 
hf = (L/D)* (a*V + b*V**2)
print ('A energia dissipada é', hf)
