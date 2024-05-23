# Módulos

import numpy as np

# Programa Principal

rng = np.random.default_rng(seed=42)

# O rng é um gerdor de arrays. A seed serve para fixar os números sorteados, ou seja, qualquer um com a mesma seed terá os mesmos números que o seu. Por padão usam o número 42, mas podemos colocar qualquer número inteiro.

vendas_mes = rng.integers(low=20, high=200, size=30, endpoint=True) 

# Chamanos o gerador de arrays e passamos alguns parâmetros. intergers(indica que o gerador irá gerar somente números inteiros) low: Valor mínimo que deve ser gerado; high: Valor máximo a ser gerado; size: Tamanho do array; endpoint: indica que o limite(high) será pode ser incluso no array.

vendas_por_semana = np.reshape(vendas_mes, (5, 6)) 

# Método reshape serve para reorganizar o array em matrizes, informamos somente o número de linhas e colunas que desejamos.

vendas_cada_semana = np.sum(vendas_por_semana, axis=1) 

# Método de soma de um array. No caso, por ser uma matriz existe 02 eixos, portanto definimos se queremos que some colunas ou linhas pelo parâmetro axis, sendo '1' somar por linhas e '0' somar por coluna.

media_semana = np.mean(vendas_por_semana, axis=1) 

# Método mean faz a média dos valores do array seguinto o parâmetro 'axis' que você informar.

vendas_dia_semana = np.sum(vendas_por_semana, axis=0)
media_dia = np.mean(vendas_por_semana, axis=0)
print(f'O total de vendas por semana de seg-sab foi {vendas_cada_semana}, a média de vendas por semana {media_semana} e a media de vendas por dia da semana foi {media_dia}')
