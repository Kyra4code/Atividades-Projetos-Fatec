import os;
import sys;
import gettext;
import time;
from time import sleep;
from transatio import translation;

#Codigozin bonitin

#programa comecando
os.system("cls")
print("Programa inicado");

sleep(1.5);

print("Configurando idioma");

#configuracao do idioma
try:
    _ = translation();
    sleep(2);
    print(_("Idioma configurado com sucesso"));
    sleep(1.3);
except:
    print("Idioma não configurado com sucesso");


#--------------------------------------------------------------------------------------------------------------------------------
def QuestaoA():

    # os.system("cls");

    C= 0;
    F = (9 * C -160)/5;

    print(F, "\n");

    sleep(4);

# QuestaoA()

#--------------------------------------------------------------------------------------------------------------------------------
def QuestaoC():

    # os.system("cls");

    pi = 3.14;
    altura = 0;
    raio = 0;
    volume = pow(raio,2) * pi  * altura;

    print(volume, "\n");

    sleep(4);

# QuestaoC();

#--------------------------------------------------------------------------------------------------------------------------------
def QuestaoD():

    # os.system("cls");

    tempo = float(input(_("Qual o tempo percorrido? \n")));
    vel_media = float(input(_("Qual a velocidade media percorrida? \n")));

    distancia = vel_media * tempo;
    consumo = distancia / 12;

    print(consumo, "\n");

    sleep(4);

QuestaoD();

#--------------------------------------------------------------------------------------------------------------------------------
def QuestaoE():

    # os.system("cls");

    tempo = 0;
    valor = 0;
    taxa = 0;
    prestacao = valor + (valor * taxa/100) * tempo;

    print(prestacao, "\n");

    sleep(4);

# QuestaoE();

#--------------------------------------------------------------------------------------------------------------------------------
def QuestaoH():

    # os.system("cls");

    L = 0;
    A = 0;
    C = 0;
    volume = C * A * L;

    print(volume, "\n");

    sleep(4);

# QuestaoH()
