import os

def clear():
    os.system( "cls" if os.name == "nt" else "clear")

def controle():

    clear()

    print("Oque voce gostaria de fazer?\n")

    try:

        response = int(input(
            "1. Inserir linha\n"
            "2. Mostrar\n"
            "3. Sair\n"
            "R:"
        ))

    except:
        response = None

    return response
    
nome = [
    "Sara Lemes", 
    "Ricardo Jafé"
]

salario = [
    12000, 
    10243.20
]

idade=[
    30, 
    45
]

def atv_01():
    while True:

        menu = controle()

        if menu == 1:
            clear()
            new_name = input("Insira um nome\nR:")
            clear()
            new_salario = input("Digite o salario\nR:")
            clear()
            new_age = input("Digite a idade\nR:")

            nome.append(new_name)
            salario.append(new_salario)
            idade.append(new_age)

            clear()
            input("Nova linha salva com sucesso")
            continue



        if menu == 2:
            count_lines = 1
            for i in range(len(nome)):
                count_lines += i
            
            clear()
            choise:int = int(input("qual linha deseja mostrar? (Comeca da linha 0)\nR:"))

            if choise > count_lines:
                input("Essa linha nao existe")
                continue

            else:
                input(f"Nome: {nome[choise]}, Idade: {idade[choise]}, Salario: {salario[i]}")
                continue

        if menu == 3:
            break

        else:
            input("Opcao invalida")

atv_01()
