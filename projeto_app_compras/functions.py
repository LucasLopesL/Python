from time import sleep
from pathlib import Path
import json


def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade


def remover_item(compras, item):
    if item in compras:
        del compras[item]
    else:
        print(f'O item {item} não existe. Tente novamente.')


def visualizar_lista(compras):
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}\n')
    print("Precione 'Enter' para continuar")
    input()


def salvar_lista(compras, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(compras, arquivo)


def carregar_lista(nome_arquivo):
    with open(f'{nome_arquivo}.json', "r") as arquivo:
        return json.load(arquivo)

    
def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        print("1. Adicionar Item\n2. Remover Item\n3. Visualizar Lista\n4. Salvar e Sair\n5. Sair sem Salvar")
        escolha = int(input("Escolha uma opção: "))
        if escolha == 1:
            item = str(input("Qual item deseja adicionar: "))
            quantidade = int(input("Digite a quantidade: "))
            adicionar_item(compras, item, quantidade)
        elif escolha == 2:
            item = str(input("Digite o nome do item que deseja remover: "))
            remover_item(compras, item)
        elif escolha == 3:
            visualizar_lista(compras)
        elif escolha == 4:
            if nome_arquivo is None:
                nome_arquivo = str(input("Digite  o nome da lista de compras: "))
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"
            salvar_lista(compras, nome_arquivo)
            break
        elif escolha == 5:
            break
        else:
            print("Opção inválida. Tente Novamente.")
            sleep(1)

            