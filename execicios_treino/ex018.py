class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentar_salario(self, aumento):
        aumento = float(input('Digite o aumento salarial em porcentagem: '))
        self.salario += self.salario * (aumento/100)

nome = str(input('Digite o seu nome: '))
salario = float(input('Digite o seu salário: '))
funcionario1 = Funcionario(nome, salario)

funcionario1.aumentar_salario(funcionario1.nome, funcionario1.salario)
