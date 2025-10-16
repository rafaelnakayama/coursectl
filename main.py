import students_functions as sf

def main_menu():
    Check = False

    print("\n__ MENU PRINCIPAL __\n")
    print("1) Cadastrar alunos")
    print("2) Visualizar alunos")
    print("3) Sair")

    while (Check == False):
        try:
            option = int(input("\nSelecione uma das opcoes Acima: "))

            if option >= 1 and option <= 3:
                print(f"Opção {option} selecionada.")
                Check = True
            
            else:
                print(f"Caractere {option} inválido.")
        except:
            print(f"Caractere provavelmente não é inteiro.")
            Check = False
    

main_menu()