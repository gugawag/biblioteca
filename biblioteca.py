from aluno import Aluno
from emprestimo import Emprestimo
from livro import Livro

class Biblioteca:

    def __init__(self, codigo, endereco):
        self.codigo = codigo
        self.endereco = endereco
        self.livros = []
        self.alunos = []
        self.funcionarios = []
        self.emprestimos = []

    def get_codigo(self):
        return self.codigo

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def get_alunos(self):
        return self.alunos

    def cadastrar_aluno(self, aluno):
        for alunoAtual in self.alunos:
            if alunoAtual.get_matricula() == aluno.get_matricula():
                raise ValueError('Matrícula já cadastrada')
        self.alunos.append(aluno)

    def realizar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def imprimir_alunos(self):
        for aluno in self.alunos:
            print(aluno)

    def imprimir_emprestimos_ativos(self):
        for emprestimo in self.emprestimos:
            if not emprestimo.foiDevolvido():
                print(emprestimo)
