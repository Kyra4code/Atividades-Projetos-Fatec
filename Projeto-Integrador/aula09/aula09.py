import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def controle():

    clear()

    print("Oque voce gostaria de fazer?\n")

    try:

        response = int(input(
            "1. Inserir valor\n"
            "2. Calcular o fatorial\n"
            "3. Mostrar o calculo do fatorial\n"
            "4. Sair\n"
            "R:"
        ))

    except:
        response = None

    return response



def atv_1():

    clear()
    a = int(input("Insira um valor inteiro\n"))
    clear()
    b = int(input("Insira um outro valor inteiro\n"))

    result = 0

    for i in range(a, b + 1):

        check = i % 2

        if(check != 0):
            result += i

    print(f"A soma dos numeros impares e: {result}")

def atv_2():

    value = 0
    result = 0 


    while True:

        option = controle()

        if option == 1:

            clear()

            value = int(input("Insira o valor do inteiro:\nR: "))

        elif option == 2:

            clear()

            if value == 0:
                clear()
                input("Por favor, insira um valor antes")
                continue

            for i in range(value):


                if(i == 0):
                    result = 1

                else:
                    result *= i

            input("Resultado calculado com sucesso")
            continue

        elif option == 3:
            if(value == 0 or result == 0):
                clear()
                input("Por favor, Calcule tudo antes.\n")
                continue
            
            clear()
            print(f"O valor do resultado: {result}")

            input("\nPress a keycap")

        elif option == 4:
            break

        else:
            clear()
            input("Opção inválida. (Enter)")


atv_1()




