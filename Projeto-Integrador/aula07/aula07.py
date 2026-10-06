from ast import While
from urllib import response
from time import *
import os
from sys import *

#metodo sleep usa segundos

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():

    clear()

    print("Oque voce gostaria de fazer?\n")

    try:

        response = int(input(
            "1. Inserir o valor da prestacao e a quantidade de dias\n"
            "2. Calcular o valor da multa\n"
            "3. Mostrar o valor calculado\n"
            "4. Sair\n"
            "R:"
        ))

    except:
        response = None

    return response


def main():

    clear()

    print("Bem Vindo ao programa para calcular multa !!\n")
    sleep(1.5)

    value = None
    days = None
    multa = None
    juros = None
    v_pagar = None
    
    while True:

        clear()

        selection = menu()

        if(selection == 1):
            
            clear()

            value = int(input("Insira o valor da prestacao: \n"))

            clear()
            
            days = int(input("Insira a quantidade de dias: \n"))

        elif(selection == 2):

            if(days is None or value is None):

                clear()
                input("Por favor, Insira os dias e o valor da prestacao antes.\n")
                continue

            multa = 0.02 * value
            juros = 0.01 * 1/30 * days * value
            v_pagar = value + multa + juros

            clear()
            print("Calculado com sucesso")
            sleep(1)

        elif(selection == 3):

            if(multa is None or juros is None or v_pagar is None):

                clear()
                input("Por favor, Calcule tudo antes.\n")
                continue
            
            clear()
            print(f"O valor da prestacao vai ser: {value}")
            print(f"A quantidade de dias foi: {days}")
            print(f"O o juros foi {juros}")
            print(f"A multa foi {multa}")
            print(f"O valor a pagar vai ser: {v_pagar}")

            input("\nPress a keycap")

        elif(selection == 4):
            break

        else:
            clear()
            input("Insira uma das opcoes validas no menu. Por favor!")
            continue

main()

