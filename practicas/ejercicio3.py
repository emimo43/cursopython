"""Problema:
Realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto"""

def suma():
    num1 = int(input("Favor ingrese el primer numero: "))
    num2 = int(input("Favor ingrese el segundo numero: "))

    

    resultado = num1 + num2
    resultado2 = num1 * num2
    return resultado,resultado2
    

     


print(suma())
