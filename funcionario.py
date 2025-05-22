
class Funcionario:

    quantidade_funcionarios = 0

    BIBLIOTECARIO = 1
    SERVICOS_GERAIS = 2

    def __init__(self,
                 matricula,
                 cpf,
                 nome,
                 salario=1585,
                 tipo_funcionario=BIBLIOTECARIO):
        self.__matricula = matricula
        self.__cpf = cpf
        self.__nome = nome
        self.__salario = salario
        self.__tipo_funcionario = tipo_funcionario
        Funcionario.quantidade_funcionarios += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == '123X':
            raise ValueError('Nome impróprio!')
        self.__nome = novo_nome

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def get_salario(self):
        return self.__salario

    def aumentar_salario(self, aumento):
        if aumento <= 0:
            raise ValueError('Aumento inválido!')
        self.__salario += aumento


    def __str__(self):
        return self.__nome

# test-drive
print('QFunc:', Funcionario.quantidade_funcionarios)

f1 = Funcionario('123', '999.999.999-99',
                 'Antônio Carlos da Silva',
                 3000)

f2= Funcionario('124', '999.999.999-98',
                 'Carlos da Silva')



print('F1:', f1.nome)
f1.nome = '123X'
print('F1:', f1.nome)

# print('F2:', f2)
#
# print('QFunc:', f1.quantidade_funcionarios)
# print('QFunc:', f2.quantidade_funcionarios)
#
#
# # print(f1.get_salario())
# # f1.aumentar_salario(-3000)
# # print(f1.get_salario())
#
# print(Funcionario.BIBLIOTECARIO)
# print(Funcionario.SERVICOS_GERAIS)
