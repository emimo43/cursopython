'''
    Ejercicio 11 --> Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo
'''
# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Ahora generamos el ciclo if para obtener la informacion requerida
if numero1 > numero2:
    # Generamos la suma y la resta
    suma = numero1 + numero2
    resta = numero1 - numero2
    # Ahora mostramos por consola el resultado
    print(f"El resultado de la suma es: {suma}\nEl resultado de la resta es: {resta}\nFin del programa")
else:
    # Generamos la multiplicacion y division
    producto = numero1 * numero2
    division = numero1 / numero2
    divisionEntera = numero1 // numero2
    # Ahora mostramos por consola el resultado
    print(f"El resultado de la multiplicacion es: {producto}\nEl resultado de la division es: {division}\nEl resultado de la division entera es: {divisionEntera}\nFin del programa")