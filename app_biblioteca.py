from aluno import Aluno
from livro import Livro
from emprestimo import Emprestimo
from biblioteca import Biblioteca

# test-drive

# criar biblioteca
biblioteca = Biblioteca('123', 'Rua A, 123')

# cadastrar alunos
aluno1 = Aluno('123', 'Gustavo Wagner')
aluno2 = Aluno('124', 'Yan Douglas')

biblioteca.cadastrar_aluno(aluno1)
biblioteca.cadastrar_aluno(aluno2)

print("=== Alunos Cadastrados ===")
biblioteca.imprimir_alunos()

# cadastrar livros

livro1 = Livro('123', 'Aprendendo Python', '978-3-16-148410-0', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro2 = Livro('124', 'Aprendendo Java', '978-3-16-148410-1', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro3 = Livro('125', 'Aprendendo C++', '978-3-16-148410-2', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')
livro4 = Livro('126', 'Aprendendo JavaScript', '978-3-16-148410-3', ['Gustavo Wagner', 'João Silva'], '2023-10-01', 'Tecnologia')

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)
biblioteca.cadastrar_livro(livro4)

print("\n=== Livros Cadastrados ===")
biblioteca.imprimir_livros()

# realizar empréstimo
emprestimo1 = Emprestimo(123, '2025-05-07', [livro1], aluno1, '2025-06-15')

biblioteca.realizar_emprestimo(emprestimo1)

print("\n=== Empréstimos Ativos ===")
biblioteca.imprimir_emprestimos_ativos()
