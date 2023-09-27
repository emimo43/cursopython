"""Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor que el segundo informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo"""

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Ahora realizamos la condicion if
if (numero1 > numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La suma del {numero1} con el {numero2} es: {suma}")
    print(f"La resta del {numero1} con el {numero2} es: {resta}")

else:
    producto = numero1 * numero2
    division = numero1 / numero2

    print(f"La Multiplicacion del {numero1} con el {numero2} es: {producto}")
    print(f"La Division del {numero1} con el {numero2} es: {division}")
