import os
from math import *


def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def menu():
    limpar()
    return input(
        "Bem vindo ao sistema de cálculo de Bhaskara\n\n"
        "0. Inserir valores dos coeficientes\n"
        "1. Calcular os possíveis valores de X\n"
        "2. Imprimir os resultados dos valores de X\n"
        "3. Sair do sistema\n"
        "R: "
    )


def main():
    a = b = c = None
    x1 = x2 = None
    calculado = False

    while True:
        
        opcao = menu()

        limpar()

        if opcao == "0":

            while True:
                a = ler_float("Valor de A: ")
                if a != 0:
                    break

                print("A não pode ser 0 (não seria equação do 2º grau).")

            b = ler_float("Valor de B: ")
            c = ler_float("Valor de C: ")
            calculado = False

        elif opcao == "1":
            if a is None:
                input("Insira o valor dos coeficientes primeiro! (Enter)")
                continue

            delta = b**2 - 4 * a * c

            if delta < 0:
                x1 = x2 = None
                calculado = True
                input("Delta negativo: não há raízes reais. (Enter)")

            else:
                x1 = (-b + sqrt(delta)) / (2 * a)
                x2 = (-b - sqrt(delta)) / (2 * a)
                calculado = True
                input("Cálculo concluído! (Enter)")

        elif opcao == "2":

            if not calculado:
                input("Calcule o valor de X primeiro! (Enter)")

            elif x1 is None:
                input("Não há raízes reais para esta equação. (Enter)")

            else:
                print(f"x1 = {x1}\nx2 = {x2}")
                input("\n(Enter para voltar)")

        elif opcao == "3":

            if input("Certeza que deseja sair? (S/n) ").lower() != "n":
                break

        else:
            input("Opção inválida. (Enter)")


main()