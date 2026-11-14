import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def lern() -> int:

    while True:
        try:
            return int(input("Digite um número: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def calpar(n: int) -> int:
    
    return sum(1 for x in range(1, n + 1) if x % 2 == 0)


def calimpar(n: int) -> int:
   
    return sum(x for x in range(1, n + 1) if x % 2 != 0)


def exibir(n: int, par: int, impar: int) -> None:
   
    print(f"n = {n}")
    print(f"Quantidade de pares de 1 a {n}: {par}")
    print(f"Soma dos ímpares de 1 a {n}: {impar}\n")
    input()

def main() -> None:
    n, totpar, totimpar, tecla = 0, 0, 0, 0

    while tecla != 4:

        print("\n1 Ler número\n2 Calcular\n3 Exibir\n4 Sair")

        try:
            tecla = int(input("Opção: "))

        except ValueError:
            print("Opção inválida.")
            continue

        if tecla == 1:
            clear()
            n = lern()
            clear()

        elif tecla == 2:
            clear()
            totpar = calpar(n)
            totimpar = calimpar(n)

            input("Calculo feito com sucesso")
            clear()
            continue


        elif tecla == 3:
            clear()
            exibir(n, totpar, totimpar)
            clear()

        elif tecla == 4:
            print("Final")
            break

        else:
            print("Opção inválida.")

main()