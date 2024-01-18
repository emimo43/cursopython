"""Cree un programa que al recivir como datos dos numeros enteros, calcule la suma, resta y multiplicacion de dichos numeros"""

# Generamos la funcion es numerico para validar si el numero es entero
def es_numerico(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False


# Solicitamos los datos al usuario
numero1 = (input("Favor ingrese el primer numero entero: "))
numero2 = (input("Favor ingrese el segundo numero entero: "))

if es_numerico(numero1) and es_numerico(numero2):     
    print("Ha digitado un valor valido.")
    numero1 = int(numero1)
    numero2 = int(numero2)
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    print(f"El valor de la suma es: {suma}")
    print(f"El valor de la resta es: {resta}")
    print(f"El valor de la multiplicacion es: {multiplicacion}")
else:
    print("El valor digitado no corresponde con un numero entero")    


