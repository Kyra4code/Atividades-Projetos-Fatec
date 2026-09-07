import os
import sys
import time
from math import *

def calc_IMC():

    nome = input("Qual seu nome ? \nR: ")

    peso = float(input("Qual seu peso? \nR: "))
    altura = float(input("Qual sua altura? \nR:"))

    imc = peso / pow(altura, 2)

    #Validacoes
    if (imc < 18.5):
        print(f"{nome}, voce esta abaixo do peso!\nSeu Imc foi de {imc:.2f}")

    elif(imc <= 24.9 and imc > 18.5):
        print(f"{nome}, voce esta no peso ideal! eu Imc foi de {imc:.2f}")

    elif(imc > 24.9):
        print(f"{nome}, voce esta acima do peso! eu Imc foi de {imc:.2f}")

calc_IMC()
