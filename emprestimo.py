from aluno import Aluno

class Emprestimo:

    def __init__(self, codigo, data_emprestimo, livros,
                 aluno, data_vencimento, data_devolucao=None, multa=None):
        self.codigo = codigo
        self.data_emprestimo = data_emprestimo
        self.livros = livros
        self.aluno = aluno
        self.data_vencimento = data_vencimento
        self.data_devolucao = data_devolucao
        self.multa = multa

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo

    def get_data_emprestimo(self):
        return self.data_emprestimo

    def set_data_emprestimo(self, nova_data):
        self.data_emprestimo = nova_data

    def get_livros(self):
        return self.livros

    def set_livros(self, novos_livros):
        self.livros = novos_livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def get_aluno(self):
        return self.aluno

    def set_aluno(self, novo_aluno):
        self.aluno = novo_aluno

    def get_data_vencimento(self):
        return self.data_vencimento

    def set_data_vencimento(self, nova_data):
        self.data_vencimento = nova_data

    def get_data_devolucao(self):
        return self.data_devolucao

    def set_data_devolucao(self, nova_data):
        self.data_devolucao = nova_data

    def get_multa(self):
        return self.multa

    def set_multa(self, nova_multa):
        self.multa = nova_multa

    def foiDevolvido(self):
        return self.data_devolucao is not None

    def __str__(self):
        return f'Empréstimo {self.codigo} - Aluno: {self.aluno.nome} - Livros: {[livro.titulo for livro in self.livros]} - Data de Empréstimo: {self.data_emprestimo} - Data de Vencimento: {self.data_vencimento} - Data de Devolução: {self.data_devolucao} - Multa: {self.multa if self.multa else 0}'


