import pytest
from app import create_app, db
from app.models import Aluno, Turma
from flask import url_for

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'  # Banco de dados em memória para testes
    })

    with app.app_context():
        db.create_all()
        # Criar uma turma para os testes
        turma = Turma(descricao="Turma 1", professor_id=1, ativo=True)
        db.session.add(turma)
        db.session.commit()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_aluno(client):
    # Criar um novo aluno
    response = client.post(url_for('aluno_bp.create_aluno'), json={
        'nome': 'João',
        'idade': 20,
        'turma_id': 1,
        'data_nascimento': '2004-05-10',
        'nota_primeiro_semestre': 8.5,
        'nota_segundo_semestre': 9.0
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Aluno criado com sucesso!'

def test_get_alunos(client):
    # Listar todos os alunos (deve estar vazio no início)
    response = client.get(url_for('aluno_bp.get_alunos'))
    assert response.status_code == 200
    assert response.json == []

    # Criar um aluno
    client.post(url_for('aluno_bp.create_aluno'), json={
        'nome': 'Maria',
        'idade': 21,
        'turma_id': 1,
        'data_nascimento': '2003-06-15',
        'nota_primeiro_semestre': 7.5,
        'nota_segundo_semestre': 8.0
    })

    # Listar novamente os alunos
    response = client.get(url_for('aluno_bp.get_alunos'))
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_aluno(client):
    # Criar um aluno
    client.post(url_for('aluno_bp.create_aluno'), json={
        'nome': 'Pedro',
        'idade': 22,
        'turma_id': 1,
        'data_nascimento': '2002-01-12',
        'nota_primeiro_semestre': 6.5,
        'nota_segundo_semestre': 7.5
    })

    # Obter o aluno pelo ID
    response = client.get(url_for('aluno_bp.get_aluno', id=1))
    assert response.status_code == 200
    assert response.json['nome'] == 'Pedro'

def test_update_aluno(client):
    # Criar um aluno
    client.post(url_for('aluno_bp.create_aluno'), json={
        'nome': 'Ana',
        'idade': 19,
        'turma_id': 1,
        'data_nascimento': '2005-03-09',
        'nota_primeiro_semestre': 7.0,
        'nota_segundo_semestre': 8.5
    })

    # Atualizar o aluno
    response = client.put(url_for('aluno_bp.update_aluno', id=1), json={
        'nome': 'Ana Clara',
        'idade': 20,
        'turma_id': 1,
        'data_nascimento': '2005-03-09',
        'nota_primeiro_semestre': 7.5,
        'nota_segundo_semestre': 9.0
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Aluno atualizado com sucesso!'

def test_delete_aluno(client):
    # Criar um aluno
    client.post(url_for('aluno_bp.create_aluno'), json={
        'nome': 'Carlos',
        'idade': 18,
        'turma_id': 1,
        'data_nascimento': '2006-11-20',
        'nota_primeiro_semestre': 6.0,
        'nota_segundo_semestre': 6.5
    })

    # Deletar o aluno
    response = client.delete(url_for('aluno_bp.delete_aluno', id=1))
    assert response.status_code == 204
