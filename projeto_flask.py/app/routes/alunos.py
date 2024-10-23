from flask import Blueprint, request, jsonify
from app.models import Aluno, db

aluno_bp = Blueprint('aluno_bp', __name__)

# Criar um novo aluno
@aluno_bp.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.get_json()
    aluno = Aluno(
        nome=data['nome'], 
        idade=data['idade'], 
        turma_id=data['turma_id'], 
        data_nascimento=data['data_nascimento'], 
        nota_primeiro_semestre=data['nota_primeiro_semestre'], 
        nota_segundo_semestre=data['nota_segundo_semestre']
    )
    db.session.add(aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno criado com sucesso!'}), 201

# Listar todos os alunos
@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    alunos_data = [
        {
            'id': aluno.id,
            'nome': aluno.nome,
            'idade': aluno.idade,
            'turma_id': aluno.turma_id,
            'data_nascimento': aluno.data_nascimento.strftime('%Y-%m-%d'),
            'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
            'nota_segundo_semestre': aluno.nota_segundo_semestre,
            'media_final': aluno.media_final
        } for aluno in alunos
    ]
    return jsonify(alunos_data), 200

# Atualizar um aluno existente
@aluno_bp.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    data = request.get_json()
    
    aluno.nome = data['nome']
    aluno.idade = data['idade']
    aluno.turma_id = data['turma_id']
    aluno.data_nascimento = data['data_nascimento']
    aluno.nota_primeiro_semestre = data['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = data['nota_segundo_semestre']
    
    db.session.commit()
    return jsonify({'message': 'Aluno atualizado com sucesso!'}), 200

# Deletar um aluno
@aluno_bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({'message': 'Aluno deletado com sucesso!'}), 204

# Obter um aluno específico
@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    aluno_data = {
        'id': aluno.id,
        'nome': aluno.nome,
        'idade': aluno.idade,
        'turma_id': aluno.turma_id,
        'data_nascimento': aluno.data_nascimento.strftime('%Y-%m-%d'),
        'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
        'nota_segundo_semestre': aluno.nota_segundo_semestre,
        'media_final': aluno.media_final
    }
    return jsonify(aluno_data), 200
