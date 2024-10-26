import pytest
from flask import Flask
from projeto_flask import app, database
from projeto_flask.controller.forms import criarProfessor, criarAluno, criarTurma
from projeto_flask.models.models import Professor, Aluno, Turma

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            database.create_all()  # Cria as tabelas do banco de dados
        yield client
        database.drop_all()  # Limpa o banco de dados após os testes

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'homepage' in response.data  # Verifique se a string 'homepage' está na página

def test_create_professor(client):
    response = client.post('/create', data={
        'nome': 'Professor Teste',
        'idade': 30,
        'materia': 'Matemática',
        'observacoes': 'Observação Teste',
        'confirmacao_create_prof': 'true'
    })
    assert response.status_code == 302  # Redirecionamento para homepage
    with app.app_context():
        professor = Professor.query.filter_by(nome='Professor Teste').first()
        assert professor is not None

def test_create_aluno(client):
    # Primeiro, você pode precisar criar uma turma para associar ao aluno
    turma = Turma(nome='Turma Teste', descricao='Descrição Teste', ativo=True)
    database.session.add(turma)
    database.session.commit()

    response = client.post('/create', data={
        'nome': 'Aluno Teste',
        'idade': 20,
        'turma_id': turma.id,  # ID da turma criada
        'data_nascimento': '2004-10-10',
        'nota_semestre1': 8.5,
        'nota_semestre2': 9.0,
        'media': 8.75,
        'confirmacao_create_aluno': 'true'
    })
    assert response.status_code == 302  # Redirecionamento para homepage
    with app.app_context():
        aluno = Aluno.query.filter_by(nome='Aluno Teste').first()
        assert aluno is not None

def test_create_turma(client):
    response = client.post('/create', data={
        'nome': 'Turma Teste',
        'descricao': 'Descrição Teste',
        'professor_id': None,  # Adicione o ID de um professor se necessário
        'ativo': True,
        'confirmacao_create_turma': 'true'
    })
    assert response.status_code == 302  # Redirecionamento para homepage
    with app.app_context():
        turma = Turma.query.filter_by(nome='Turma Teste').first()
        assert turma is not None

def test_update_professor(client):
    # Cria um professor antes de tentar atualizá-lo
    professor = Professor(nome='Professor Original', idade=30, materia='Matemática', observacoes='Observação Original')
    database.session.add(professor)
    database.session.commit()

    response = client.post('/update', data={
        'id': professor.id,
        'nome': 'Professor Atualizado',
        'idade': 31,
        'materia': 'Matemática Avançada',
        'observacoes': 'Observação Atualizada',
        'confirmacao_update_prof': 'true'
    })
    assert response.status_code == 302  # Redirecionamento para homepage
    with app.app_context():
        updated_professor = Professor.query.get(professor.id)
        assert updated_professor.nome == 'Professor Atualizado'

def test_delete_professor(client):
    # Cria um professor antes de tentar deletá-lo
    professor = Professor(nome='Professor Para Deletar', idade=30, materia='Matemática', observacoes='Observação Para Deletar')
    database.session.add(professor)
    database.session.commit()

    response = client.post('/delete', data={
        'id': professor.id,
        'confirmacao_delete_prof': 'true'
    })
    assert response.status_code == 302  # Redirecionamento para homepage
    with app.app_context():
        deleted_professor = Professor.query.get(professor.id)
        assert deleted_professor is None  # O professor deve ter sido deletado
