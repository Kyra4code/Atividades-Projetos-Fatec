import os;
import sys;
import gettext;
import time;
from time import sleep;
from transatio import translation;

#nt e a indentificacao do wuindows e posix do linux

if(os.name == 'nt'):
    os.system("cls")

if(os.name == 'posix'):
    os.system("clear")

def Inicializacao():
    print("Programa inicado");

    sleep(1.5);

    print("Configurando idioma");

    try:
        _ = translation();
        sleep(2);
        print(_("Idioma configurado com sucesso"));
        sleep(1.3);
    except:
        print("Idioma não configurado com sucesso");


def atividadeA():

    Inicializacao()

    base = 2
    altura = 2

    area = base * altura /2

    print(area, "\n")

    sleep(1.2)
    print("Encerrando sistema")
    sleep(1.5)

atividadeA()

def atividadeB():

    Inicializacao()

    Tempo = 0

    Distancia = Tempo * 340

    print(Distancia)

    sleep(1.2)
    print("Encerrando sistema")
    sleep(1.5)


def atividadeC():
    G = 9.8
    Altura  = 0
    TQ = ((2*Altura) ** 0.5) / G

    print(TQ)

atividadeC()

def atividadeD():

    Perimetro = 0
    Pi = 3.14
    Diametro = Perimetro /Pi
    Raio = Diametro / 2
    Area = Raio * Raio * Pi

    print(Area)

atividadeD()


print("ATV_A")
sleep(3)


print("ATV_B")
sleep(3)
atividadeB()
