import students_functions as sf
import csv
import datetime

def main_menu():
    Check = False

    # meus_alunos = []

    hoje = datetime.datetime.now()

    print("\n__ MENU PRINCIPAL __\n")
    print("1) Cadastrar alunos")
    print("2) Visualizar alunos")
    print("3) Sair")

    print(f"\n" + hoje.strftime("%x"))

    while (Check == False):
        try:
            option = int(input("\nSelecione uma das opcoes Acima: "))

            if option == 1:

                nome_do_aluno = str(input("Informe o nome do aluno: "))

                status_do_aluno = str(input("Este aluno está tendo aulas? (S/N): ")).upper()
                if status_do_aluno == "S":
                    status_do_aluno = "Ativo"
                elif status_do_aluno == "N":
                    status_do_aluno = "Deligado"
                else:
                    status_do_aluno = "UNKNOWN"

                aulas_assistidas = int(input("Informe quantas aulas o aluno assistiu: "))

                data_do_pagamento = str(input("Informe a data do pagamento: "))

                nivel_do_aluno = str(input("Informe o nível do aluno: "))

                # novo_aluno = sf.cadastrar_aluno(nome_do_aluno, status_do_aluno, aulas_assistidas, data_do_pagamento, nivel_do_aluno)

                with open("students.csv", "a", newline='') as arquivocsv:
                    chaves_csv = ["Nome: ", "Status: ", "Aulas: ", "Dia do Pagamento: ", "Nivel: "]
                    escritor = csv.DictWriter(arquivocsv, chaves_csv=chaves_csv)

                    escritor.writeheader()
                    escritor.writerow({'Nome: ': f'{nome_do_aluno}', 'Status: ': f'{status_do_aluno}', 'Aulas: ': f'{aulas_assistidas}', 'Dia do Pagamento: ': f'{data_do_pagamento}', 'Nivel: ': f'{nivel_do_aluno}'})

                # meus_alunos.append(novo_aluno)


            elif option == 2:
                with open("students.csv", newline='') as arquivocsv:
                    leitor_csv = csv.reader(arquivocsv, delimiter=' ', quotechar='|')
                    for linha in leitor_csv:
                        print(', '.join(linha))

            elif option == 3:
                break

            else:
                print(f"A Opção '{option}' não exite.")

        except:
            print(f"Este Caractere provavelmente não é inteiro.")
            Check = False
    
main_menu()