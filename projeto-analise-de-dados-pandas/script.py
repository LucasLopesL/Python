import pandas as pd


funcionarios_df = pd.read_csv(r'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto-analise-de-dados-pandas\CadastroFuncionarios.csv', sep=';', decimal=',')

clientes_df = pd.read_csv(r'C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto-analise-de-dados-pandas\CadastroClientes.csv', sep=';', decimal=',')

servicos_df = pd.read_excel(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto-analise-de-dados-pandas\BaseServiçosPrestados.xlsx")


# Folha Salarial

funcionarios_df["Salário Total"] = funcionarios_df["Salario Base"] + funcionarios_df["Impostos"] + funcionarios_df["Beneficios"] + funcionarios_df["VT"] + funcionarios_df["VR"]
folha_salarial = sum(funcionarios_df["Salario Base"])
print(f'O total gasto com folha salarial é de R${folha_salarial:,.2f}')


# Faturamento da empresa

faturamento_df = servicos_df.merge(clientes_df, on='ID Cliente')
faturamento_empresa = sum(faturamento_df["Valor Contrato Mensal"] * faturamento_df["Tempo Total de Contrato (Meses)"])
print(f'O faturamento total da empresa foi de R${faturamento_empresa:,.2f}')

# % Funcionários que fecharam contrato

funcionarios_com_contratos = len(servicos_df["ID Funcionário"].unique()) / funcionarios_df["ID Funcionário"].count()
print(f'A % de funcionários que fecharam contrato é de: {funcionarios_com_contratos:.2%}')


# QTY Contratos por área

contratos_df = servicos_df.merge(funcionarios_df, on="ID Funcionário")
contratos_area = contratos_df["Area"].value_counts()
print(f'A Quantidade de contratos por área é {contratos_area}')


# Funcionários por área

funcionarios_area = funcionarios_df["Area"].value_counts()
print(f'A quantidade de funcionários por área é {funcionarios_area}')


# Ticket médio mensal

ticket_medio = clientes_df["Valor Contrato Mensal"].mean()
print(f'O ticket médio do contratos mensais é de R${ticket_medio:,.2f}')
