import students_functions as sf
import datetime

def main_menu():
    Check = False

    meus_alunos = []

    hoje = datetime.datetime.now()

    print("\n__ MENU PRINCIPAL __\n")
    print("1) Cadastrar alunos")
    print("2) Visualizar alunos")
    print("3) Sair")

    print(hoje)

    while (Check == False):
        try:
            option = int(input("\nSelecione uma das opcoes Acima: "))

            if option == 1:
                nome_do_aluno = str(input("Informe o nome do aluno: "))
                status_do_aluno = str(input("Este aluno está tendo aulas? (S/N): ")).upper()
                if status_do_aluno == "S":
                    status_do_aluno == "Ativo"
                elif status_do_aluno == "N":
                    status_do_aluno == "Deligado"
                else:
                    status_do_aluno == "UNKNOWN"
                data_do_pagamento = str(input("Informe a data do pagamento: "))
                nivel_do_aluno = str(input("Informe o nível do aluno: "))

                sf.cadastrar_aluno(nome_do_aluno, status_do_aluno, data_do_pagamento, nivel_do_aluno)

                meus_alunos.append(nome_do_aluno)

            elif option == 2:
                for x in meus_alunos:
                    print(x)

            elif option == 3:
                break

            else:
                print(f"A {option} não exite.")
        except:
            print(f"Caractere provavelmente não é inteiro.")
            Check = False
    
main_menu()