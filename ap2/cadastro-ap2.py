# Alunos: 

# Lucas Lopes -> R.A:2303315; 
# Luigi Costabile Brum -> R.A:;
# Enzo Dancona de Souza -> R.A:

# Módulos

from time import sleep
from sqlalchemy import create_engine, text, Column, Integer, String, Float, ForeignKey, Varchar
from sqlalchemy.orm import DeclarativeBase, Session

# Configuração de Conexão com o Banco de dados SQLITE

engine = create_engine("sqlite:///server.db")

# Script para ciração das tabelas no Banco de dados

with engine.connect() as connection:
    result = connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                                ID INTEGER PRIMARY KEY,
                                NOME VARCHAR(255),
                                CPF VARCHAR(255),
                                IDADE INTEGER)""")
    
connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")

# Inicia a sessão com o banco de dados

session = Session(engine)

# Classe Base/Padão do SQLALCHEMY

class Base(DeclarativeBase):
    pass


# Definição das classes da tabela

class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String (255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):   # Construtor
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', Integer)
    especializacao = Column('ESPECIALIZAÇÃO', String(255))

    def __init__(self, nome, crm, especializacao):   # Construtor
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True)
    id_medico = Column(Integer, ForeignKey('medico.id'))
    id_paciente = Column(Integer, ForeignKey('id.paciente'))
    descricao = Column(Varchar(255))
    resultado = Column(Varchar(255))


# Funções


def cadastrar_medico():
    
    '''
    Função que cadastra um Médico.
    1º O usuário faz um série de "inputs" e os que são do tipo "str" são tratados para evitar erros futuros para consultas no Banco de dados pelo método "strip()" que retira os espaços antes e depois do dado inserido.
    2º É declarado uma variável "medico" que armazena um objeto da classe "Medico" e atribui os valores inseridos pelo usuário nas colunas corretas da tabela "MEDICO".
    3º É criado uma sessão com o banco de dados junto do objeto "medico" pronto para ser inserido dentro da base de dados.
    4º Solicitamos a confimarção do usuário quanto aos dados inseridos. 
    5º Validamos o "input" da confirmação deixando tudo em letras minúsculas e tirando os espaços para evitar erros.
    6º Caso o usuário indique a certeza, o objeto "medico" será inserido de vez dentro do banco de dados pelo método "commit()". Se o usuário não confirmar a veracidade dos dados eles não serão 'comitados'/confirmados dentro do banco de dados.

    Parâmetros:
    Nenhum

    Return: 
    Cadastra um medico dentro da tabela "MEDICO" do banco de dados.
    '''

    nome = str(input('Digite o Nome do médico: ')).strip()
    crm = int(input('Digite o CRM do médico (Sem Pontuação): '))
    especializacao = str(input("Digite a especialixação do médico: ")).strip()
    medico = Medico(nome=nome, crm=crm, especializacao=especializacao)
    Session.add(medico)
    confirmacao = str(input('Você tem certeza dos dados inseridos? (S/N)')).casefold().strip()
    if confirmacao == 's':
        Session.commit()
    else:
        print('Dados descartados com sucesso!')
    print('Médico cadastrado com sucesso!')


def cadastrar_paciente():
    
    '''
    Função que cadastra um paciente.
    1º O usuário faz um série de "inputs" e os que são do tipo "str" são tratados para evitar erros futuros para consultas no Banco de dados pelo método "strip()" que retira os espaços antes e depois do dado inserido.
    2º É declarado um variável "paciente" que armazena um objeto da classe "Paciente" e atribui os valores inseridos pelo usuário nas colunas corretas da tabela "PACIENTE".
    3º É criado uma sessão com o banco de dados junto do objeto "paciente" pronto para ser inserido dentro da base de dados.
    4º Solicitamos a confimarção do usuário quanto aos dados inseridos. 
    5º Validamos o "input" da confirmação deixando tudo em letras minúsculas e tirando os espaços para evitar erros.
    6º Caso o usuário indique a certeza o objeto "paciente" será inserido de vez dentro do banco de dados pelo método "commit()". Se o usuário não confirmar a veracidade dos dados eles não serão 'comitados'/confirmados dentro do banco de dados.

    Parâmetros:
    Nenhum

    Return: 
    Cadastra um paciente dentro da tabela "PACIENTE" do banco de dados.
    '''

    nome = str(input('Digite o nome do Paciente: ')).strip()
    cpf = int(input('Digite o CPF do paciente (Sem pontuação): '))
    idade = int(input('Digite a idade do paciente:'))
    paciente = Paciente(nome=nome, cpf=cpf, idade=idade)
    Session.add(paciente)
    confirmacao = str(input('Você tem certeza dos dados inseridos? (S/N): ')).casefold().strip()
    if confirmacao == 's':
        Session.commit()
    else:
        print('Dados descartados com sucesso!')
    print('Paciente cadastrado com sucesso!')


def cadastrar_exame():

    '''
    Função que cadastra exame.
    1º O usuário faz um série de "inputs" e os que são do tipo "str" são tratados para evitar erros futuros para consultas no Banco de dados pelo método "strip()" que retira os espaços antes e depois do dado inserido.
    2º É declarado uma variável "exame" que armazena um objeto da classe "Exame" e atribui os valores inseridos pelo usuário nas colunas corretas da tabela "EXAME".
    3º É criado uma sessão com o banco de dados junto do objeto "exame" pronto para ser inserido dentro da base de dados.
    4º Solicitamos a confimarção do usuário quanto aos dados inseridos. 
    5º Validamos o "input" da confirmação deixando tudo em letras minúsculas e tirando os espaços para evitar erros.
    6º Caso o usuário indique a certeza o objeto exame será inserido de vez dentro do banco de dados pelo método "commit()". Se o usuário não confirmar a veracidade dos dados eles não serão 'comitados'/confirmados dentro do banco de dados.

    Parâmetros:
    Nenhum

    Return: 
    Cadastra um exame dentro da tabela "EXAME" do banco de dados.
    '''

    id_medico = int(input('Digite o ID do médico responsável pelo exame: '))
    id_paciente = int(input('Digite o ID do paciente que fará o exame: '))
    descricao = str(input('Descrição do exame: ')).strip()
    resultado = str(input('Resultado do exame: ')).strip()
    exame = Exame(id_medico=id_medico, id_paciente=id_paciente, descricao=descricao, resultado=resultado)
    Session.add(exame)
    confirmacao = str(input('Você tem certeza dos dados inseridos? (S/N): ')).casefold().strip()
    if confirmacao == 's':
        Session.commit()
    else:
        print('Dados descartados com sucesso!')
    print('Exame cadastrado com sucesso!')


def consultar_exames():

    '''
    Programa que consulta exames de determinado paciente;
    1º O usuário insere o ID do paciente que deseja consultar o exame.
    2º É feito uma "query" (Solicitação) na tabela Exame dentro do banco de dados que filtra a solicitação de acordo com o ID do paicente (método "filter_by") e retorna todos os resultados encontrados (método "all()").
    3º Verfica se a lista retornada da consulta está vazia ("if exames:")
    4º Caso a lista não estiver vazia para cada objeto dentro da lista ele irá retornar um "print" com o ID do exame, a descrição e o resultado. Caso não encontre nem um exame ele retornara outro print indicando que não encontrou nenhum exame para aquele paciente.

    Parâmetros:
    Nenhum

    Return:
    Retorna os exames de determinado paciente.
    '''

    id_paciente = int('Digite o ID do paciente que deseja consultar o exame: ')
    exames = session.query(Exame).filter_by(id_paciente=id_paciente).all()
    if exames:
        for exame in exames:
            print(f"ID do Exame: {exame.id}, Descrição: {exame.descricao}, Resultado: {exame.resultado}")
    else:
        print("Nenhum exame encontrado para este paciente.")
    

# Programa Principal


nome = str(input('Digite seu nome: ')).strip()
sleep(0.2)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print(f'Bem-vindo ao Programa de Cadastro, Dr(a).{nome}\n')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
sleep(0.5)

while True: 
    print('MENU:\n1. Cadastrar Médico\n2.Cadastrar Paciente\n3.Cadastrar Exame\n4.Consultar Exames\n5.Encerrar Programa')
    opcao = str(input('Digite a opção desejada: ')).strip()
    if opcao == '1':
        cadastrar_medico()
    elif opcao == '2':
        cadastrar_paciente()
    elif opcao == '3':
        cadastrar_exame()
    elif opcao == '4':
        consultar_exames()
    elif opcao == '5':
        print('Encerrando o programa...')
        sleep(1)
        print('Programa encerrado com sucesso!')
        break
    else:
        print('Opção inválida. Tente novamente...')
