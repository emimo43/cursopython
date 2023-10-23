"""Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos"""

# Solicitamos los datos del Usuario
num1 = int(input("Favor ingrese el primer numero: "))
num2 = int(input("Favor ingrese el segundo numero: "))
num3 = int(input("Favor ingrese el tercer numero: "))

# Ahora comenzamos con el ciclo if para comparar lo solicitado
if(num1 > num2 and num1 > num3):
    print(f"El {num1} es el mayor")
else:
    if(num2 > num1 and num2 > num3):
        print(f"El {num2} es el mayor")
    else:
        print(f"El {num3} es el mayor")