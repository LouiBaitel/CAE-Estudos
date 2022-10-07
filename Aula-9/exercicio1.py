'''EXERCÍCO 1 - PESO DOS BOIS'''
#PESO DOS BOIS

bois = [560, 340.9, 456.89, 900, 398.78, 334, 765, 999, 560, 900]

#leitura dos pesos dos bois e armazenamento na lista
quant= int(input('QUANTOS BOIS? '))
for b in range (quant):
        bois.append (float(input ('Peso do boi '+str (b+1)+': ')))

    
#IMPRIMIR O PESO E O IDENTIFICADOR DO BOI
for i in range (len(bois)):
    print ('Boi',i+1, ' peso =', bois[i] )
    
#identificar o boi com maior peso
maior = max (bois)
for i in range (len(bois)):
    if (bois [i]== maior):
        print ('O boi mais pesado e', i+1, 'com', bois[i], 'kg' )
        break