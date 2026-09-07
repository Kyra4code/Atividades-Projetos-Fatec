import os
import sys
import time
from math import *

def atividade_C():

    A = 2
    B = -3
    C = -5
    delta = (pow(B,2) - 4 * A * C)

    if(delta < 0):
        print("Essa equacao e uma equacao incompleta")
        return

    x1 = (B * -1) + (sqrt(delta)) / (2 * A)
    x2 = (B * -1) - (sqrt(delta)) / (2 * A)

    print("x1 = ", x1, "e x2 = ", x2)

atividade_C()


def atividade_A():
    maior = 4
    menor = 2
    subtracao = 4 - 2

    if(maior > menor):
        print(f"O resultado da diferenca:",maior - menor)
    else:
        print(f"variavel maior precisa sem maior que a menor")


atividade_A()

def atividade_B():
    num_escolhido = -5

    if(num_escolhido < 0):
        print(num_escolhido * -1)
    else:
        print(num_escolhido)

atividade_B()

