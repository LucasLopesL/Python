# AVALIAÇÃO PARCIAL 1

# Aluno 1: Lucas Lopes
# Aluno 2: Luigi Brum Costabile
# Aluno 3: Enzo Dancona de Souza
# Aluno 4: Pedro Henrique Pila Julião

import random

# -------------------------------- CLASSES -----------------------------------------

class ContaBancaria:
    def __init__(self, correntista, saldo):
        self.__correntista = correntista
        self.__saldo = saldo
        self.__senha = self.criar_senha()
        self.__cpmf = 0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
        self.__cpmf += valor * 0.0025  # Calcula o valor do imposto (0.25%)

    def transferir(self, valor, conta_destino):
        if isinstance(conta_destino, ContaBancaria):
            if self.__saldo >= valor:
                self.__saldo -= valor
                conta_destino.depositar(valor)
                self.__cpmf += valor * 0.0025  # Calcula o valor do imposto (0.25%)
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo insuficiente para realizar a transferência.")
        else:
            print("Conta de destino inválida.")

    def criar_senha(self):
        return ''.join(random.choices('0123456789', k=6))

    def get_saldo(self):
        return self.__saldo

    def get_senha(self):
        return self.__senha

    def get_cpmf(self):
        return self.__cpmf

    def exibir_info(self):
        return f"Conta de {self.__correntista} - Saldo de R$ {self.__saldo:.2f}"

# -------------------------------- FUNÇÕES -----------------------------------------

def mostrar_info(contas):
    print("\nContas de todos os clientes:")
    for i, conta in enumerate(contas):
        print(f"[{i}] {conta.exibir_info()}")

def interacao_sacar(contas):
    cliente_valido = False
    while not cliente_valido:
        mostrar_info(contas)
        indice_conta = int(input(f"O saque será efetuado na conta de qual cliente? (0 a {len(contas) - 1}): "))
        if 0 <= indice_conta < len(contas):
            cliente_valido = True
        else:
            print("Índice de cliente inválido!")
    saque = float(input("Qual o valor do saque? "))
    contas[indice_conta].sacar(saque)
    print("Saque finalizado.")

def interacao_depositar(contas):
    cliente_valido = False
    while not cliente_valido:
        mostrar_info(contas)
        indice_conta = int(input(f"O depósito será efetuado na conta de qual cliente? (0 a {len(contas) - 1}): "))
        if 0 <= indice_conta < len(contas):
            cliente_valido = True
        else:
            print("Índice de cliente inválido!")
    deposito = float(input("Qual o valor do depósito? "))
    contas[indice_conta].depositar(deposito)
    print("Depósito finalizado.")

def interacao_transferir(contas):
    cliente_valido_origem = False
    while not cliente_valido_origem:
        mostrar_info(contas)
        indice_origem = int(input(f"Transferência a partir da conta de qual cliente? (0 a {len(contas) - 1}): "))
        if 0 <= indice_origem < len(contas):
            cliente_valido_origem = True
        else:
            print("Índice de cliente inválido!")

    cliente_valido_destino = False
    while not cliente_valido_destino:
        mostrar_info(contas)
        indice_destino = int(input(f"Transferir para a conta de qual cliente? (0 a {len(contas) - 1}): "))
        if 0 <= indice_destino < len(contas) and indice_destino != indice_origem:
            cliente_valido_destino = True
        else:
            print("Índice de cliente inválido ou igual à origem!")

    valor_transferencia = float(input("Qual o valor da transferência? "))
    contas[indice_origem].transferir(valor_transferencia, contas[indice_destino])

# --------------------------- PROGRAMA PRINCIPAL -----------------------------------
    
contas = [
    ContaBancaria("Marcos", 1000.00),
    ContaBancaria("Júlia", 250.00),
    ContaBancaria("João", 2500.00),
    ContaBancaria("Roberto", 3000.00),
    ContaBancaria("Janaína", 4500.00)
]

while True:
    print("Escolha uma operação:")
    print("(1) mostrar informações de todas as contas")
    print("(2) sacar")
    print("(3) depositar")
    print("(4) transferir")
    print("(5) sair")
    escolha = int(input("Opção escolhida: "))
    if escolha == 1:
        mostrar_info(contas)
    elif escolha == 2:
        interacao_sacar(contas)
    elif escolha == 3:
        interacao_depositar(contas)
    elif escolha == 4:
        interacao_transferir(contas)
    elif escolha == 5:
        print("Fim do programa!")
        break
    else:
        print("Opção inválida!")

print()
