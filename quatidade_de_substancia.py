'''calcule n para quaisquer valores de P, V, T
n => quantidade de substÃ¢ncia
'''
R = 8.31446261815324  # constante do gás ideal

#ENTRADA DE DADOS
P = float (input('Valor da pressao: '))
V = float (input('Valor do volume: '))
T = float (input('Valor da temperatura: '))



#CALCULO DE n - quantidade de substancia
n = (P*V) / (R*T)
print ('A quantidade de substancia e', round (n,3))
