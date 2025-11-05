import students_functions as sf
import ui_functions as ui

def main_menu():
    Check = False

    sf.verificar_csv()

    ui.menu_interface()

    while (Check == False):
        try:
            option = int(input("\n\033[32mSelecione uma das opcoes acima: \033[0m"))
        except ValueError:
            print("\033[1;31mO caractére inserido não é inteiro.\033[1;31m")
            Check = False
            continue
        except:
            print("\033[1;31mOutra coisa deu errada.\033[1;31m")
            Check = False
            continue

        if option == 1:
            # Captura os valores que existem dentro de ui.inputs_cadastro()
            id_aluno, nome_aluno, status_aluno, aulas_aluno, pagamento_aluno, nivel_aluno = ui.inputs_cadastro()

            novo_Aluno = sf.cadastrar_aluno(id_aluno,
                                            nome_aluno, 
                                            status_aluno, 
                                            aulas_aluno,
                                            pagamento_aluno,
                                            nivel_aluno,)
            print("\n")
            ui.menu_interface()

        elif option == 2:
            sf.visualizar_alunos()
            ui.menu_interface()

        elif option == 3:
            # Chama o menu de Editar Aluno
            ui.menu_option_3()

            # Nome
            alterar_por_nome = str(input("\n\033[38;5;208mInforme o do aluno a ser editado: \033[0m"))
            sf.aluno_existe(alterar_por_nome)

            while (sf.aluno_existe(alterar_por_nome) == False):
                print("\033[1;31mEste aluno não está no banco de dados.\033[0m")
                alterar_por_nome = str(input("\033[32mInforme o nome do aluno: \033[0m"))

            # Chama os inputs do editar, e associa os valores do return às variaveis locais.
            chave, valor_atualizado = ui.inputs_editar()

            sf.editar_aluno(alterar_por_nome, chave, valor_atualizado)

            print("\n")
            ui.menu_interface()

        elif option == 4:
            nome_aluno = str(input("\033[32mInforme o nome do aluno: \033[1;31m")).lower()
            sf.aluno_existe(nome_aluno)

            while (sf.aluno_existe(nome_aluno) == False):
                print("\033[1;31mEste aluno não está no banco de dados.\033[1;31m")
                nome_aluno = str(input("\033[32mInforme o nome do aluno: \033[1;31m"))

            sf.remover_aluno(nome_aluno)

            print("\n")
            ui.menu_interface()

        elif option == 5:
            # chama o menu Materiais
            ui.menu_materiais()

            Validar = False
            
            while(Validar == False):
                try:
                    opcao = int(input("\n\033[38;5;208mSelecione uma das opcoes acima: \033[0m"))
                except ValueError:
                    print("\033[1;31mO caractére inserido não é inteiro.\033[1;31m")
                    Validar = False
                    continue
                except:
                    print("\033[1;31mOutra coisa deu errada.\033[1;31m")
                    Validar = False
                    continue

                if opcao == 1:
                    print("\033[38;5;208m(1) Aulas, (2) Textos ou (3) Exercicios\033[0m")
                    Validar_2 = False
                    while (Validar_2 == False):
                        try:
                            tipo_material = int(input("\n\033[38;5;208mSelecione o Material: \033[0m"))
                            if tipo_material not in [1, 2, 3]:
                                raise ValueError("\033[1;31mFora do intervalo.\033[0m")
                            Validar_2 = True
                        except ValueError as e:
                            if str(e) == "fora_do_intervalo":
                                print("\033[1;31mO valor deve estar entre 1 e 3.\033[0m")
                            else:
                                print("\033[1;31mO caractére inserido não é inteiro.\033[0m")
                            continue
                        except Exception:
                            print("\033[1;31mOutra coisa deu errada.\033[0m")
                            continue

                elif opcao == 3:
                    print("\n\033[1;35mRetornando ao menu principal\033[1;35m")
                    Validar = True

                elif opcao == 4:
                    Validar = True
                    Check = True
                    print("\n\033[1;35mSaindo do programa...\033[1;35m")

                else:
                    print(f"\033[1;31mA Opção '{opcao}' não exite.\033[1;35m")

                ui.menu_interface()           

        elif option == 6:
            print("\n\033[1;35mSaindo do programa...\033[1;35m")
            Check = True

        else:
            print(f"\033[1;31mA Opção '{option}' não exite.\033[1;35m")
    
main_menu()