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


# Importando base de dados da Internet

exportacoes_df = pd.read_csv(r"C:\Users\lucas\OneDrive\Área Pessoal\MeusProjetos\Python\Python\projeto-analise-de-dados-pandas\exportacoes_franca.csv", sep=",", decimal=",")


# Evolução das exportções de 2016 a 2020

def formatar(valor):
    valor_formatado = f'US$ {valor:,.2f}'
    return valor_formatado


evolucao_df = exportacoes_df[["Year", "US$ FOB"]].groupby("Year").sum()
evolucao_df = evolucao_df["US$ FOB"].apply(formatar)
print(f"A Evolução das exportações na França do ano de 2016 até o ano de 2020 foi\n {evolucao_df}")


# Quais os produtos mais exportados ao longo do período

produtos_df = exportacoes_df[["SH2 Description", "US$ FOB"]].groupby("SH2 Description").sum(numeric_only=True).sort_values(by="US$ FOB", ascending=False)
produtos_df = produtos_df["US$ FOB"].apply(formatar)
print(f'Os Produtos mais exportados ao longo do período foram\n{produtos_df}')


# Em 2020 qual cidade mais exportou na França

exportacoes_2020_df = exportacoes_df.loc[exportacoes_df["Year"] == 2020, :]
exportacoes_2020_df = exportacoes_2020_df[["City", "US$ FOB"]].groupby("City").sum(numeric_only=True).sort_values(by="US$ FOB", ascending=False)
exportacoes_2020_df = exportacoes_2020_df["US$ FOB"].apply(formatar)
print(f'A cidade que mais exportou em 2020 foi: \n {exportacoes_2020_df}')


# Quais os produtos mais exportados em (US$) que as 02 maiores cidades (em exportação exportaram)

tabela_2020 = exportacoes_df.loc[exportacoes_df["Year"] == 2020, :]
tabelas_cidades_2020 = tabela_2020[["City", "US$ FOB"]].groupby("City").sum()
tabelas_cidades_2020 = tabelas_cidades_2020.sort_values(by="US$ FOB", ascending=False)
tabelas_cidades_2020["US$ FOB"] = tabelas_cidades_2020["US$ FOB"].apply(formatar)
cidade = tabelas_cidades_2020.index[0]
tabela_cidade = tabela_2020.loc[tabela_2020["City"] == cidade, :]
tabela_produto_cidade = tabela_cidade[["SH2 Description", "US$ FOB"]].groupby("SH2 Description").sum()
tabela_produto_cidade = tabela_produto_cidade.sort_values(by="US$ FOB", ascending=False)
tabela_produto_cidade["US$ FOB"] = tabela_produto_cidade["US$ FOB"].apply(formatar)
print(f'Os produtos mais exportados da cidade {cidade} são:\n {tabela_produto_cidade}')
