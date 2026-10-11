# -*- coding: utf-8 -*-
import os
import sys
from time import sleep

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def lerN1():
    n1 = float ( input ('Nota1:'))
    return n1

def lerN2():
    n2 = float ( input ('Nota2:'))
    return n2

'''

A palavra get se refere a pegar algum dado.
A palavra melhor utilizada seria calc ou general_media (media_geral)

'''

def calc_media(n1, n2):

    media = (n1+n2)/2
    return media

def mostrar(media):

    clear()
    print(f'\nMédia = {media}')
    
    if media < 6: 
        print('\nAluno Reprovado')

    else:
        print('\nAluno Aprovado')

        '''

        (DICA !!!)

        Esse sleep nao funciona 
        (Pelo menos nao no linux). 
        A melhor opcao seria usar o sleep do modulo python, 
        ou criar um def assim fiz para o clear)

        '''
        
        sleep(5)


def menu():

    clear()

    print("Oque voce gostaria de fazer?\n")

    try:

        response = int(input(
            "1. Inserir as notas dos alunos\n"
            "2. Calcular a media\n"
            "3. Mostrar a media\n"
            "4. Sair\n"
            "R:"
        ))

    except:
        response = None

    return response


def main():

    nota1 = None
    nota2 = None
    media = None

    while True:

        option = menu()

        if option == 1:
            nota1 = lerN1()
            nota2 = lerN2()

        elif option == 2:

            if nota1 is None or nota2 is None:

                clear()
                input("Por favor, insira o as notas antes")
                continue

            media = calc_media(nota1, nota2)

        elif option == 3:
        
            if media is None:

                clear()
                input("Por favor, calcule a media antes")
                continue

            mostrar(media)

        elif option == 4:
            clear()
            break

        else:
            clear()
            input("Opção inválida. (Enter)")
        

main()
sys.exit 