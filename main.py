import students_functions as sf
import ui_functions as ui

def main_menu():
    Check = False

    ui.menu_interface()

    while (Check == False):
        try:
            option = int(input("\nSelecione uma das opcoes Acima: "))
        except ValueError:
            print("Este Caractere provavelmente não é inteiro.")
            Check = False
            continue
        except:
            print(f"Outra coisa deu errada.")
            Check = False
            continue


        if option == 1:
            # Clean
            
            # Captura os valores que existem dentro de ui.inputs_cadastro()
            nome_aluno, status_aluno, aulas_aluno, pagamento_aluno, nivel_aluno = ui.inputs_cadastro()

            novo_Aluno = sf.cadastrar_aluno(nome_aluno, 
                                            status_aluno, 
                                            aulas_aluno,
                                            pagamento_aluno,
                                            nivel_aluno,)

        elif option == 2:
            sf.visualizar_alunos()

        elif option == 3:

            alterar_por_nome = str(input("Informe o nome do aluno: "))
            sf.aluno_existe(alterar_por_nome)

            while (sf.aluno_existe(alterar_por_nome) == False):
                print("\033[1;31mEste aluno não está no banco de dados.\033[0m")
                alterar_por_nome = str(input("Informe o nome do aluno: "))

            chave = None
            valor_atualizado = None

            ui.menu_option_3()

            selecao = int(input("Selecione um valor: "))

            if selecao == 1:
                chave = 'Nome'
                valor_atualizado = str(input("Insira o novo Nome: "))
            elif selecao == 2:
                chave = 'Status'
                valor_atualizado = str(input("Insira o novo Status: "))
            elif selecao == 3:
                chave = 'Aulas'
                valor_atualizado = int(input("Informe a quantidade de Aulas: "))
            elif selecao == 4:
                chave = 'Dia do Pagamento'
                valor_atualizado = str(input("Insira o novo dia de Pagamento: "))
            elif selecao == 5:
                chave = 'Nivel'
                valor_atualizado = str(input("Insira o novo Nivel: "))

            sf.editar_aluno(alterar_por_nome, chave, valor_atualizado)

        elif option == 4:
            # Clean
            nome_aluno = str(input("Informe o nome do aluno: "))
            sf.aluno_existe(nome_aluno)

            while (sf.aluno_existe(nome_aluno) == False):
                print("\033[1;31mEste aluno não está no banco de dados.\033[1;31m")
                nome_aluno = str(input("Informe o nome do aluno: "))

            sf.remover_aluno(nome_aluno)

        elif option == 5:
            # Clean
            print("\n\033[1;35mSaindo do programa...\033[1;35m")
            break

        else:
            # Clean
            print(f"\033[1;31mA Opção '{option}' não exite.\033[1;35m")
    
main_menu()