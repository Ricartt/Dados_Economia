# -*- coding: utf-8 -*-
"""Economia per capita.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_IRDk-rIsXHoE21ix8_aNSnCh5oQPomA

**Dados econômicos**
---
Dados da renda per capita dos estados da união

link oficial dos dados: http://www.atlasbrasil.org.br/
"""

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

bd = pd.read_excel("Dados_Pib.xlsx")

bd.head(10)

# Agrupando por território
bd.groupby(by=['Territorialidades', 'Ano']).mean()  # -->média

# Grid de graficos

# Cor
cor_fundo = '#f5f5f5'

# Sistema de grids
graficos = sns.FacetGrid(bd, col='Territorialidades', hue='Territorialidades', col_wrap=4)

# Adicionando gráfico de linhas em cada gráfico
graficos= graficos.map(plt.plot, 'Ano','PIB per capita' )
                  # parâmetro map para gráfico em especifico
# Adicionando sombra
graficos = graficos.map(plt.fill_between,'Ano','PIB per capita', alpha=0.2 ).set_titles('{col_name} Territorialidades')
graficos = graficos.set_titles('{col_name}')

# Adicionando subtitulos
graficos = graficos.fig.suptitle('Evolução da Renda Per Capita por Estado',fontsize=18)

plt.subplots_adjust(top=0.92)