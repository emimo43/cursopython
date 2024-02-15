'''
Tarea 2: Clasificación de números en rangos.
    Escribe un programa Python que solicite al usuario ingresar un número entero y luego determine en qué rango se encuentra ese número utilizando la declaración match. El programa debe imprimir un mensaje que indique el rango al que pertenece el número.
'''
numero = int(input("Favor ingrese un numero entero: "))

match numero:
    case numero if numero < 0:
        print(f"El numero ingresado {numero} es negativo, Rango 1")
    case numero if numero >= 0 and numero < 10:
        print(f"El numero ingresado {numero} es positivo, Rango 2")
    case numero if numero >= 10:
        print(f"El numero ingresado {numero} es positivo, Rango 3")    
    case _:
        print("Numero no reconocido")        