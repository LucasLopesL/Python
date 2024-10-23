from flask import Blueprint, request, jsonify
from app.models import Turma, db

turma_bp = Blueprint('turma_bp', __name__)

# Criar uma nova turma
@turma_bp.route('/turmas', methods=['POST'])
def create_turma():
    data = request.get_json()
    turma = Turma(
        descricao=data['descricao'], 
        professor_id=data['professor_id'], 
        ativo=data.get('ativo', True)
    )
    db.session.add(turma)
    db.session.commit()
    return jsonify({'message': 'Turma criada com sucesso!'}), 201

# Listar todas as turmas
@turma_bp.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = Turma.query.all()
    turmas_data = [
        {
            'id': turma.id,
            'descricao': turma.descricao,
            'professor_id': turma.professor_id,
            'ativo': turma.ativo
        } for turma in turmas
    ]
    return jsonify(turmas_data), 200

# Atualizar uma turma existente
@turma_bp.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    turma = Turma.query.get_or_404(id)
    data = request.get_json()
    
    turma.descricao = data['descricao']
    turma.professor_id = data['professor_id']
    turma.ativo = data.get('ativo', turma.ativo)
    
    db.session.commit()
    return jsonify({'message': 'Turma atualizada com sucesso!'}), 200

# Deletar uma turma
@turma_bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'message': 'Turma deletada com sucesso!'}), 204

# Obter uma turma específica
@turma_bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = Turma.query.get_or_404(id)
    turma_data = {
        'id': turma.id,
        'descricao': turma.descricao,
        'professor_id': turma.professor_id,
        'ativo': turma.ativo
    }
    return jsonify(turma_data), 200
