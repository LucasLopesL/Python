# Módulos
from random import shuffle, choice, choices
import string

# Funções

def gerar_senha(comprimento):

    '''
        Função que recebe como parâmetro o comprimento que a senha terá.
    1º validamos se o tamanho é acima do mímino aceitável (4 caractéres).
    2º garantimos os requisitos mínimos da senha (pelo menos uma letra, um dígito e um caracter especial).
    3º colocamos as posibilidades de letras maiúsculas e minúsculas, digitos e caracteres especiais que possam completar a senha com os demais dígitos para atender o comprimento solicitado pelo usuário.
    4º Como os 3 primeiros dígitos da senha estão em uma lista, geramos outra lista e a transformamos em um conjunto de strings e juntamos os outros carateres sorteados na lista dos 3 primeiros dígitos. Para isso usamos o método "extend".
    5º Emparalhamos a senha pelo método "shuffle".
    6º transformamos a lista (senha) final em um conjunto de strings e a retornamos como resultado.

    --------------------------------------

    *Parâmetros*
    comprimento: int

    --------------------------------------

    Return:
    senha: str

    '''

    if comprimento < 4:
        print('O comprimento da senha deve ser mais que 4 caracteres!')
    else:
        senha = [
            choice(string.ascii_letters),
            choice(string.digits),
            choice(string.punctuation)
        ]
        
        possibilidades = "".join([string.ascii_letters, string.digits, string.punctuation])

        senha.extend(choices(possibilidades, k=comprimento-3))

        shuffle(senha)

        return "".join(senha)
    
print('')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('')
print('Bem vindo ao gerador de senhas seguras!')
print('')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('')

tamanho = int(input("Digite o tamanho da senha desejada: "))
print(gerar_senha(tamanho))