from math import *
import os

os.system("clear")

a = float(input("Insira a medida de lado 1\nR:"))
b = float(input("Insira a medida de lado 2\nR:"))
c = float(input("Insira a medida da base\nR:"))
    
if a + b <= c or a + c <= b or b + c <= a:
    print("Esses valores não formam um triângulo.")

else:
        p = (a + b + c) / 2
        area = sqrt(p * (p-a) * (p-b) * (p-c) )         
                
        print(f"De acordo ao teorema de HERON. A area do triangulo pussui: {area:.2f}")