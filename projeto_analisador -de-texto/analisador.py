# Importação dos Módulos

import string 
from collections import Counter

# Funções

def analisar_texto(texto):
    
    '''
    A função recebe como par^metro um texto que é tratado pela remoção da pontuação com o método 'maketrans'.
    Em seguida, o texto será dividido entre palavras dentro de uma lista.
    Para saber a quantidade de palavras que o texto possui contaremos a quantidade de itens dentro dessa lista pelo método 'len'.
    Para saber a frequencia das palavras usamos o metodo 'counter'.
    Para saber a frequencia de letras usamos novamente o método 'counter' mas com o método 'casefold', pois o python faz a distinção entre letras maiúsuclas e minúsculas.
    Por fim retornamos os valores.

    -------------------------------------------

    *Parâmetros*

    Texto: str
        Texto a ser analisado

    -------------------------------------------    

    returns

    tuple
        Contagem de palavras, frequência de palavras e frequência de letras

    '''

    texto_tratado = texto.translate(str.maketrans("","", string.punctuation))
    palavras = texto.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto_tratado.casefold())

    return contagem_palavras, frequencia_palavras, frequencia_letras

# Programa Principal

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print('')
print('Bem vindo ao analisador de texto!')
print('')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print('')

nome = str(input('Digite o seu nome:'))
nome.strip()
texto = str(input((f'Olá {nome}, digite o texto que você quer analisar:')))
print(analisar_texto(texto))
