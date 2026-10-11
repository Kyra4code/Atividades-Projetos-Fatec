from urllib import response
from time import *
import os
from sys import *
from math import *


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():

    clear()

    print("Oque voce gostaria de fazer?\n")

    try:

        response = int(input(
            "1. Inserir o valor do comprimento\n"
            "2. Calcular o diametro, raio e area\n"
            "3. Mostrar os valores calculados\n"
            "4. Sair\n"
            "R:"
        ))

    except:
        response = None

    return response

def main():

    raio = None
    diametro = None
    area = None
    comprimento = None
    pi = 3.14


    while True:

        option = menu()

        if option == 1:

            clear()

            comprimento = int(input("Insira do comprimento:\nR: "))

        elif option == 2:

            if comprimento is None:
                
                clear()
                input("Por favor, insira o valor do comprimento antes")
                continue

            diametro = comprimento
            raio = diametro/2
            area = pow(raio, 2) * pi

        elif option == 3:
            if(diametro is None or raio is None or area is None):
                clear()
                input("Por favor, Calcule tudo antes.\n")
                continue
            
            clear()
            print(f"O valor do diametro: {diametro}")
            print(f"AO valor do raio: {raio}")
            print(f"O valor da area: {area}")

            input("\nPress a keycap")

        elif option == 4:
            break


        else:
            clear()
            input("Opção inválida. (Enter)")


main()