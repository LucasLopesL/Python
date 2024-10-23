import pytest
from app import create_app, db
from app.models import Turma
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

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_turma(client):
    # Criar uma nova turma
    response = client.post(url_for('turma_bp.create_turma'), json={
        'descricao': 'Turma 2',
        'professor_id': 1,
        'ativo': True
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Turma criada com sucesso!'

def test_get_turmas(client):
    # Listar todas as turmas (deve estar vazio no início)
    response = client.get(url_for('turma_bp.get_turmas'))
    assert response.status_code == 200
    assert response.json == []

    # Criar uma turma
    client.post(url_for('turma_bp.create_turma'), json={
        'descricao': 'Turma 3',
        'professor_id': 1,
        'ativo': True
    })

    # Listar novamente as turmas
    response = client.get(url_for('turma_bp.get_turmas'))
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_turma(client):
    # Criar uma turma
    client.post(url_for('turma_bp.create_turma'), json={
        'descricao': 'Turma 4',
        'professor_id': 1,
        'ativo': True
    })

    # Obter a turma pelo ID
    response = client.get(url_for('turma_bp.get_turma', id=1))
    assert response.status_code == 200
    assert response.json['descricao'] == 'Turma 4'

def test_update_turma(client):
    # Criar uma turma
    client.post(url_for('turma_bp.create_turma'), json={
        'descricao': 'Turma 5',
        'professor_id': 1,
        'ativo': True
    })

    # Atualizar a turma
    response = client.put(url_for('turma_bp.update_turma', id=1), json={
        'descricao': 'Turma 5 - Atualizada',
        'professor_id': 1,
        'ativo': False
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Turma atualizada com sucesso!'

def test_delete_turma(client):
    # Criar uma turma
    client.post(url_for('turma_bp.create_turma'), json={
        'descricao': 'Turma 6',
        'professor_id': 1,
        'ativo': True
    })

    # Deletar a turma
    response = client.delete(url_for('turma_bp.delete_turma', id=1))
    assert response.status_code == 204
