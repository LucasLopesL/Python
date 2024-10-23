from flask import Blueprint, request, jsonify
from app.models import Professor, db

professor_bp = Blueprint('professor_bp', __name__)

@professor_bp.route('/professores', methods=['POST'])
def create_professor():
    data = request.get_json()
    professor = Professor(nome=data['nome'], idade=data['idade'], materia=data['materia'], observacoes=data.get('observacoes'))
    db.session.add(professor)
    db.session.commit()
    return jsonify({'message': 'Professor criado com sucesso!'}), 201

@professor_bp.route('/professores', methods=['GET'])
def get_professores():
    professores = Professor.query.all()
    return jsonify([p.nome for p in professores]), 200

@professor_bp.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    professor = Professor.query.get_or_404(id)
    data = request.get_json()
    professor.nome = data['nome']
    professor.idade = data['idade']
    professor.materia = data['materia']
    db.session.commit()
    return jsonify({'message': 'Professor atualizado!'}), 200

@professor_bp.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    professor = Professor.query.get_or_404(id)
    db.session.delete(professor)
    db.session.commit()
    return jsonify({'message': 'Professor deletado!'}), 204
