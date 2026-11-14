from math import sqrt

def atv_01():
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
        
        print(f"A area do triangulo pussui: {area}")

    elif(x == 4):
        print("A forma e um quadrado (Ou um retangulo)")

        base = float(input("Insira a medida da base\nR:"))
        altura = float(input("Insira a medida da altura\nR:"))

        area = base * altura

        print(f"A area do quadrado pussui: {area}")

    elif(x == 5 ):
        print("A forma e um pentagono")

        ld = float(input("Insira a medida de um dos lados\nR:"))
        apotema = float(input("Insira a medida da apotema\nR:"))

        p = 5 * ld

        area = p * apotema /2

        print(f"A area do pentagono pussui: {area}")

    else:
        print("Nao foi possivel indentificar o poligono")


# atv_01()

def atv_02():

    valor_01 = int(input("Insira o primeiro numero:\nR:"))
    valor_02 = int(input("Insira o segundo numero:\nR:"))
    valor_03 = int(input("Insira o terceiro numero:\nR:"))

    if(valor_01 > valor_02 and valor_01 > valor_03):
        print(f"Primeiro numero e maior que os outros ({valor_01})")

    elif(valor_02 > valor_01 and valor_02 > valor_03):
        print(f"Segundo numero e maior que os outros ({valor_02})")

    elif(valor_03 > valor_02 and valor_03 > valor_02):
        print(f"Terceiro numero e maior que os outros ({valor_03})")
    
    else:
        print(f"Todos sao iguais ou nao foi possivel identificar os a comparacao de valores")

# atv_02()

def atv_03():

    a = int(input("Insira o lado a de um triangulo"))
    b = int(input("Insira o lado b de um triangulo"))
    c = int(input("Insira o lado c de um triangulo"))

    if a <= 0 or b <= 0 or c <= 0:
        print("Os lados devem ser valores inteiros positivos.")

    else:

        if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
            print("Os valores informados NÃO formam um triângulo (apenas uma figura de três lados).")

        else:

            if a == b == c:
                tipo = "Equilatero"

            elif a == b or a == c or b == c:
                tipo = "Isosceles"

            else:
                tipo = "Escaleno"
    
            print(f"Os valores informados formam um triângulo do tipo: {tipo}")

atv_03()
