class Livro:

    def __init__(self,
                 codigo, titulo, isbn, autores,
                 data_publicacao, genero):
        self.codigo = codigo
        self.titulo = titulo
        self.isbn = isbn
        self.autores = autores
        self.data_publicacao = data_publicacao
        self.genero = genero

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, novo_isbn):
        self.isbn = novo_isbn

    def get_autores(self):
        return self.autores

    def cadastrar_autor(self, nome_autor):
        self.autores.append(nome_autor)

    def get_data_publicacao(self):
        return self.data_publicacao

    def set_data_publicacao(self, nova_data):
        self.data_publicacao = nova_data

    def get_genero(self):
        return self.genero

    def set_genero(self, novo_genero):
        self.genero = novo_genero

    def __str__(self):
        return f'ISBN {self.isbn} - Título {self.titulo}'


