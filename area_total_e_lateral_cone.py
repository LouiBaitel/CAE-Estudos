import math
#Leitura do valor da base e da altura do cone
raio = float(input('Qual o valor do raio da base do cone? ')) 
h =    float(input('Qual o valor da altura do cone? ')) 


valor = 3 * raio **3
#valor = 3 * math.pow (raio,3)

volume = (1/3)* math.pi * math.sqrt (valor)
#volume = (1/3)* math.pi *  (3*raio**3) **0 .5
#volume = (1/3)* math.pi *  (3*raio**3))**(1/2)

#volume = (1/3)* math.pi * math.sqrt (3*math.pow (raio,3)

#valor = 3*raio**3
#volume = (1/3)* math.pi * math.sqrt (valor)

#Area lateral
areaLat = 2*math.pi*raio**2
#ou areaLat = 2*math.pi*pow (raio,2)

#Area Total
areaTotal = 3*math.pi*math.pow (raio,2)

print ("Volume = ", round (volume, 2))
print ('Area Lateral  ',areaLat )
print ('Area Total ',areaTotal )