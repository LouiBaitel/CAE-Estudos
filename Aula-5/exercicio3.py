'''Exercícios Complementares Listas e Tuplas
Exercício 3
Elabore uma app em Python para ler um valor N inteiro digitado pelo usuário
e em seguida, leia uma lista de N valores. 
Por fim, imprima a soma de todos o valores divisíveis por 5 da lista e a 
lista ordenada em ordem crescente.

'''
N = int(input("Quanto valores serão lidos? "))

valores = []  #lista com os valores lidos

#Criação da lista 
for i in range (N): #for i in range (0,N,1):
    valor = float(input ("Digite o "+ str (i+1) +" valor"))
    valores.append (valor)
    
print (valores)   
    
#Verifica se o valor é divisivel por     
soma = 0
for i in range (N): #for i in range (0,N,1):
    if valores[i]%5 == 0:
        print (valores[i], 'é divisivel por 5')
        soma = soma + valores[i] #somando valores divisíveis por 5
        
print ("A soma dos valores divisiveis por 5 e", soma)

#ordenação da lista
valores.sort ()

print (valores)