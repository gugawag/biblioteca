class Aluno:

    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, nova_matricula):
        if not nova_matricula.isdigit():
            raise ValueError('Matrícula inválida')
        self.matricula = nova_matricula

    def __str__(self):
        return f'{self.matricula} - {self.nome}'

