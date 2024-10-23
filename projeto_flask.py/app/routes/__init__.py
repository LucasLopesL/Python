from app.routes.professor import professor_bp
from app.routes.turma import turma_bp
from app.routes.aluno import aluno_bp

def init_routes(app):
    app.register_blueprint(professor_bp)
    app.register_blueprint(turma_bp)
    app.register_blueprint(aluno_bp)
