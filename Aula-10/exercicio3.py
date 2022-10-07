#Exercício 3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from google.colab import files
uploaded = files.upload()

import io
dados = pd.read_csv(io.BytesIO(uploaded['UmidadeRelativa.csv']))
# Dataset is now stored in a Pandas Dataframe

#leitura dos dados 
#dados = np.loadtxt('UmidadeRelativa.csv', delimiter=';')

plt.title('Umidade relativa durante o ano com três medições ao dia')
plt.xlabel('número da medição')
plt.ylabel('taxa de umidade')

plt.plot(dados, color='g')

plt.savefig('CurvaUmidadeFleming.pdf', format='pdf')
plt.show()

x = np.linspace(50, 100, num=11)
plt.title('Distribuição das medições de umidade relativa')
plt.hist(dados, bins=x, rwidth=0.9, color='tab:purple')
plt.savefig('HistUmidadeFleming.pdf', format='pdf')


plt.show()
