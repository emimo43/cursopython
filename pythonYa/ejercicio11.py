'''
Problema:
    Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo
'''

# Solicitamos los dos numeros al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Creamos la condicion if
if numero1 > numero2:
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La suma de ambos valores es: {suma}")
    print(f"La resta de ambos numeros es: {resta}")
else:
    producto = numero1 * numero2
    division = numero1 / numero2
    print(f"El resultado de la multiplicacion es: {producto}")   
    print(f"El resultado de la division es: {round(division,2)}") # Usamos la funcion round, dentro de la funcion print
    
    
print("Fin del programa")     