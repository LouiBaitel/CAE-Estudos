'''Exercícios Complementares Listas e Tuplas
Exercício 5
Elabore uma app em Python para ler um valor inteiro N maior que 10 
e em seguida, leia uma lista de N caracteres alfanuméricos. 
Imprima o tamanho da lista, quantas vogais, 
consoantes e símbolos ela possui e a 
quantidade encontrada de cada uma das três classes. 


'''
#TUPLAS - listas com valores pré-definidos que não podem ser alterados
vogais = ('a', 'e', 'i', 'o', 'u')
consoantes = ('b', 'c','d','f','g','h','j','k','l','m','n','o','p'\
              'q','r','s','t','u','w', 'v','x', 'z')

alfanum = []
vogal = 0
consoante = 0
simbolo = 0

#usuario define a quantidade de valores da lista - deve ser > 10
N  = int(input ("Quantos caracteres serão lidos? "))

#leitura dos valores da lista
for i in range (N):
    alfanum.append (input ("Digite o caracter: "))
    
for i in range (N):
    if alfanum [i] in vogais:
        vogal = vogal+1
    elif alfanum [i] in consoantes:
        consoante = consoante + 1
    else:
        simbolo = simbolo + 1

print ('A lista contém', len(alfanum),'elementos')
print ("A quantidade de vogais e", vogal)
print ("A quantidade de consoantes e", consoante)
print ("A quantidade de simbolos e", simbolo)
    