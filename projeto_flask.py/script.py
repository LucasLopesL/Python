from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Date, Float
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# TABELAS

class Professor(Base):
    __tablename__ = "PROFESSOR"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_professor", String(45))
    idade = Column("idade_professor", String(45))
    materia = Column("materia", String(45))
    observacoes = Column("observacoes", String(200))

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes


class Aluno(Base):
    __tablename__ = "ALUNO"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome_professor", String(45))
    idade = Column('idade', Integer)
    turma = Column('turma', ForeignKey("TURMA.id"))
    data_nascimento = Column('data_nascimento', Date)
    nota_primeiro_semestre = Column('nota_primeiro_semestre', Float)
    nota_segundo_semestre = Column('nota_segundo_semestre', Float)
    media_final = Column('media_final', Float)

    def __init__(self, nome, turma, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final):
        self.nome = nome
        self.turma = turma
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final
        

class Turma(Base):
    __tablename__ = "TURMA"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String(200))
    professor = Column("professor", ForeignKey("PROFESSOR.id"))
    ativo = Column("ativo", Boolean)

    def __init__(self, descricao, professor, ativo=True):
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo


Base.metadata.create_all(bind=db)

# CRUD

# CREATE
professor = Professor(nome, idade, materia, observacoes)
session.add(professor)
session.commit()


turma = Turma(descricao, professor.id, ativo)
session.add(turma)
session.commit()

aluno = Aluno(nome, idade, turma.id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final)
session.add(aluno)
session.commit()

# READ
lista_professores = session.query(Professor).all()
professor_lucas = session.query(Professor)._filter_by(nome="Lucas").all()
print(professor_lucas)
print(professor_lucas.materia)
print(professor_lucas.observacoes)

# UPDATE

professor_lucas.nome = "Lucas Lopes"
session.add(professor_lucas)
session.commit()

# DELETE

session.delete(professor_lucas)
session.commit()

