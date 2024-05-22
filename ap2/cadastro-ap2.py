# Alunos: 

# Lucas Lopes -> R.A: 2303315; 
# Enzo Dancona de Souza -> R.A: 2302654;
# Luigi Costabile Brum -> R.A: 2302528


# Módulos

from time import sleep
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, relationship

# Configuração de Conexão com o Banco de dados SQLITE

engine = create_engine("sqlite:///server.db")


# Base para todas as classes de modelo

Base = DeclarativeBase()

# Classe Base/Padrão do SQLALCHEMY

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
    id_medico = Column("ID.MEDICO", Integer, ForeignKey('MEDICO.ID'))
    id_paciente = Column("ID_PACIENTE", Integer, ForeignKey('PACIENTE.ID'))
    descricao = Column("DESCRIÇÃO", String(255))
    resultado = Column("RESULTADO", String(255))
    medico = relationship("Medico", back_populates="exames")
    paciente = relationship("Paciente")

Medico.exames = relationship("Exame", order_by=Exame.id, back_populates="medico") # Define a relaçao entre as tabelas (Pelo método 'relationship') "Medico" e "Exame". "Exame" refere-se à classe Exame, indicando que esta relação é com a tabela Exame. O parâmetro order by indica a organização que os dados que no caso devem ser de acordo com o id da tabela Exame. Por último o parâmetro back_populates indica uma relação bilateral entre Exame e Medico, que faz com que fique fácil a relação de um exame a um médico e de um médico a um exame.

# Criação das tabelas no Banco de dados

Base.metadata.create_all(engine) #Método utilizado para criar tabelas com base em classes definidas

# Inicia a sessão com o banco de dados

Session = sessionmaker(bind=engine)
session = Session()


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
    session.add(medico)
    confirmacao = str(input('Você tem certeza dos dados inseridos? (S/N)')).casefold().strip()
    if confirmacao == 's':
        session.commit()
        print('Médico cadastrado com sucesso!')
    else:
        print('Dados descartados com sucesso!')
    

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
    session.add(paciente)
    confirmacao = str(input('Você tem certeza dos dados inseridos? (S/N): ')).casefold().strip()
    if confirmacao == 's':
        session.commit()
        print('Paciente cadastrado com sucesso!')
    else:
        print('Dados descartados com sucesso!')
    


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
    session.add(exame)
    confirmacao = str(input('Você tem certeza dos dados inseridos? (S/N): ')).casefold().strip()
    if confirmacao == 's':
        session.commit()
        print('Exame cadastrado com sucesso!')
    else:
        print('Dados descartados com sucesso!')


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

    id_paciente = int(input('Digite o ID do paciente que deseja consultar o exame: '))
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
    print('MENU:\n1.Cadastrar Médico\n2.Cadastrar Paciente\n3.Cadastrar Exame\n4.Consultar Exames\n5.Encerrar Programa')
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
