from time import sleep
import os
from functions import carregar_lista, gerenciar_compras


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1. Criar uma nova lista de Compras\n2. Carregar uma lista existente\n3. Sair")
        opcao = int(input(f'Digite a opção desejada: '))
        if opcao == 1:
            compras = {}
            gerenciar_compras(compras)
        elif opcao == 2:
            print("Listas Disponíveis:")
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]
            if not arquivos:
                print("Nenhuma lista disponível")
                sleep(2)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i}. {arquivo}\n')
            escolha = int(input("Escolha uma lista para carregar (0 para nenhuma): "))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print("Opção inválida")
                sleep(1)
                continue
            compras = carregar_lista(arquivos[escolha - 1])
            gerenciar_compras(compras, arquivos[escolha - 1])
        elif opcao == 3:
            break
        else:
            print("Opcão Inválida. Tente Novamente")
            sleep(1)


if __name__ == "__main__":
    main()
    
