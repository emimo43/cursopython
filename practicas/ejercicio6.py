"""Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto"""

# Definiremos la funcion
def suma_producto():
    num1 = int(input("Favor ingrese el primer numero: "))
    num2 = int(input("Favor ingrese el segundo numero: "))
    num3 = int(input("Favor ingrese el cuarto numero: "))
    num4 = int(input("Favor ingrese el cuarto numero: "))
    # Ahora vamos a generar la suma y el producto
    suma = num1 + num2
    producto = num3 * num4
    # Retornaremos ambas variables
    return suma,producto
    

valor_suma = suma_producto()
print(f"El valor de la suma y el producto es: {valor_suma}")