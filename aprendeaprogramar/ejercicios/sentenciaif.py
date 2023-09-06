print("hola introduce un numero positivo o negativo")
numeros = int(input())
if numeros > 0:
    print("el numero es positivo")
elif numeros < 0:
    print("este numero es negativo")
elif numeros % 2 == 0:
    print("este numero es par")
