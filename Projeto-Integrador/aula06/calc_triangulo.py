from math import *

x = int(input("Insira a quantidade de lados da forma geometrica\nR:"))
    
if(x < 3):
        print("Esse poligono nao existe")

elif(x == 3):
    print("A forma e um triangulo")

    ld_01 = float(input("Insira a medida de lado 1\nR:"))
    ld_02 = float(input("Insira a medida de lado 2\nR:"))
    base = float(input("Insira a medida da base\nR:"))
    
    p = (ld_01 + ld_02 + base) / 2

    area = sqrt(p * (p-ld_01) * (p-ld_02) * (p-base) )         
        
    print(f"De acordo ao teorema de HERON. A area do triangulo pussui: {area}")