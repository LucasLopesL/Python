import unittest
from app import create_app, database
from projeto_flask.models import Professor, Aluno, Turma

class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        database.create_all()

    @classmethod
    def tearDownClass(cls):
        database.session.remove()
        database.drop_all()
        cls.app_context.pop()

    # Teste de criação de professor
    def test_create_professor(self):
        response = self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Criação do(a) Professor(a): Prof. Teste bem sucedida!", response.data)

    # Teste de leitura de professor
    def test_read_professor(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        response = self.client.get("/read/professor")
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Prof. Teste", response.data)

    # Teste de criação de aluno
    def test_create_aluno(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        response = self.client.post("/create", data={
            'confirmacao_create_aluno': 'true',
            'nome': 'Aluno Teste',
            'idade': 20,
            'turma_id': 1,  # Supondo que a turma com ID 1 existe
            'data_nascimento': '2004-01-01',
            'nota_semestre1': 8.0,
            'nota_semestre2': 9.0,
            'media': 8.5
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Criação do(a) Aluno(a): Aluno Teste bem sucedida!", response.data)

    # Teste de leitura de aluno
    def test_read_aluno(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        self.client.post("/create", data={
            'confirmacao_create_aluno': 'true',
            'nome': 'Aluno Teste',
            'idade': 20,
            'turma_id': 1,
            'data_nascimento': '2004-01-01',
            'nota_semestre1': 8.0,
            'nota_semestre2': 9.0,
            'media': 8.5
        })
        response = self.client.get("/read/alunos")
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Aluno Teste", response.data)

    # Teste de criação de turma
    def test_create_turma(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        response = self.client.post("/create", data={
            'confirmacao_create_turma': 'true',
            'nome': 'Turma Teste',
            'descricao': 'Descrição da Turma Teste',
            'professor_id': 1,  # Supondo que o professor com ID 1 existe
            'ativo': True
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Criação da Turma: Turma Teste bem sucedida!", response.data)

    # Teste de leitura de turma
    def test_read_turma(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        self.client.post("/create", data={
            'confirmacao_create_turma': 'true',
            'nome': 'Turma Teste',
            'descricao': 'Descrição da Turma Teste',
            'professor_id': 1,
            'ativo': True
        })
        response = self.client.get("/read/turmas")
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"Turma Teste", response.data)

    # Teste de atualização de professor
    def test_update_professor(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        response = self.client.post("/update", data={
            'confirmacao_update_prof': 'true',
            'id': 1,
            'nome': 'Prof. Atualizado',
            'idade': 35,
            'materia': 'Física',
            'observacoes': 'Atualizado'
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Atualização do(a) Professor(a) ID:1 bem sucedida!", response.data)

    # Teste de atualização de aluno
    def test_update_aluno(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        self.client.post("/create", data={
            'confirmacao_create_aluno': 'true',
            'nome': 'Aluno Teste',
            'idade': 20,
            'turma_id': 1,
            'data_nascimento': '2004-01-01',
            'nota_semestre1': 8.0,
            'nota_semestre2': 9.0,
            'media': 8.5
        })
        response = self.client.post("/update", data={
            'confirmacao_update_aluno': 'true',
            'id': 1,
            'nome': 'Aluno Atualizado',
            'idade': 21,
            'turma_id': 1,
            'data_nascimento': '2004-01-01',
            'nota_semestre1': 9.0,
            'nota_semestre2': 10.0,
            'media': 9.5
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Atualização do(a) aluno(a) ID:1 bem sucedida!", response.data)

    # Teste de exclusão de professor
    def test_delete_professor(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        response = self.client.post("/delete", data={
            'confirmacao_delete_prof': 'true',
            'id': 1
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Professor ID: 1 deletado com sucesso!", response.data)

    # Teste de exclusão de aluno
    def test_delete_aluno(self):
        self.client.post("/create", data={
            'confirmacao_create_prof': 'true',
            'nome': 'Prof. Teste',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Nenhuma'
        })
        self.client.post("/create", data={
            'confirmacao_create_aluno': 'true',
            'nome': 'Aluno Teste',
            'idade': 20,
            'turma_id': 1,
            'data_nascimento': '2004-01-01',
            'nota_semestre1': 8.0,
            'nota_semestre2': 9.0,
            'media': 8.5
        })
        response = self.client.post("/delete", data={
            'confirmacao_delete_aluno': 'true',
            'id': 1
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para a homepage
        self.assertIn(f"Aluno ID: 1 deletado com sucesso!", response.data)

if __name__ == '__main__':
    unittest.main()
