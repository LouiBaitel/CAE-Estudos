#exercio 1 modificado

import matplotlib.pyplot as plt
import numpy as np

#calculo da media dos valores das notas de cada aluno e plotar o grafico alunoXmeida

eixo_x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

Notas = np.array([[5.7, 8.2, 3.4, 8.0, 6.7, 4.6, 9.1, 5.0, 2.5, 7.0],\
                 [10, 9, 9, 5, 3.7, 8.6, 9.1, 7.0, 7.5, 7.0]])
Medias =[]

#gerar os valores das medias e colocar na lista Medias
for i in range (Notas.shape [1]):
    medAluno = (Notas [0,i]+Notas [1,i])/2
    Medias.append (medAluno)


plt.plot(eixo_x, Notas [0], label ='PROVA 1')
plt.plot(eixo_x, Notas [1], label ='PROVA 2')
plt.plot (eixo_x,Medias,  label ='MEDIA')
plt.title("MEDIA DISCIPLINA")
plt.xlabel("Aluno")
plt.ylabel("Media")

plt.grid ()

plt.legend ()

plt.savefig('MEDIAS.pdf', format='pdf')


plt.show()