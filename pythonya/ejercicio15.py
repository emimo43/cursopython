'''
    Ejercicio 15 --> Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos
'''

# Solicitamos los tres numeros al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))

# Ahora generamos una estructura condicional para realizar la comparacion
if numero1 > numero2 and numero1 > numero3:
    print(f"El numero mayor es el {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El numero mayor es el {numero2}")
else:
    print(f"El numero mayor es el {numero3}")