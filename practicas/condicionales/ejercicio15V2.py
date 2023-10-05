"""Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))
num3 = int(input("Favor ingresar el tercer numero: "))

# Ingresamos al ciclo de condicionales
if(num1 > num2 and num1 > num3):
    print(num1)
else:
    if(num2 > num1 and num2 > num3):
        print(num2)
    else:
        print(num3)        