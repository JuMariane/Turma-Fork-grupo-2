alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    print("\n--- ALUNOS ---")
    print()
    for aluno in alunos:
        print(aluno)
    print()
    print("Número de alunos: " + str(len(alunos)))

while True:

    print("\n1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        break

    else:
        print("Opção inválida!")