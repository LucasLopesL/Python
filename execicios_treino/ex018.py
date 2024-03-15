class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentar_salario(self, aumento):
        self.salario += self.salario * (aumento/100)

funcionarios = []

while True:
    try:
        nome = str(input('Digite o seu nome: '))
        if nome == '':
            break
        salario = float(input('Digite o seu salário: R$ '))
        funcionario = Funcionario(nome, salario)
        funcionarios.append(funcionario)
    except ValueError:
        print('Erro! Valor inválido')

aumento = float(input('Digite o aumento em porcentagem (%): '))

for funcionario in funcionarios:
    funcionario.aumentar_salario(aumento)

for funcionario in funcionarios:
    print(f'Com o aumento seu salário será de R${funcionario.salario:,.2f}')