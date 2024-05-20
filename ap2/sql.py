# Alunos: Lucas Lopes -> R.A:2303315; Luigi Costabile Brum -> R.A:; Enzo Dancona de Souza -> R.A:

# IMPORTÇÃO DOS MÓDULOS
from sqlalchemy import create_engine, text, Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Session

# CONFIGURAÇÃO DE CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")

# SCRIPT PARA CRIAÇÃO DAS TABELAS NO BANCO DE DADOS
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

# INICIANDO SESSÃO COM BANCO DE DADOS
session = Session(engine)


# CLASSE BASE DO SQLALCHEMY
class Base(DeclarativeBase):
    pass

# DEFINIÇÃO DE CLASSE QUE MAPEIA UMA TABELA
class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String (255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):   # CONSTRUTOR
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', Integer)
    especializacao = Column('ESPECIALIZAÇÃO', String(255))

    def __init__(self, nome, crm, especializacao):   # CONSTRUTOR
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True)
