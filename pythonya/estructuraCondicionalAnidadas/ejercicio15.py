"""Problema: Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))
num3 = int(input("Favor ingresar el tercer numero: "))

# Ahora veremos el ciclo
if(num1 > num2 and num1 > num3):
    print(f"El numero mayor es el {num1}, el numero 1")
elif(num2 > num1 and num2 > num3):
    print(f"El numero mayor es el {num2}, el numero 2")
else:
    print(f"El numero mayor es el {num3}, el numero 3")        
