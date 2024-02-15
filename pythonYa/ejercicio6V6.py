'''
Problema:
    Escribir un programa en el cual se ingresan cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto
'''
# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero: ")) # Dato de tipo int
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))
numero4 = int(input("Favor ingresar el cuarto numero: "))

# Creamos las variables suma y producto para realizar el calculo solicitado
suma = numero1 + numero2
producto = numero3 * numero4

# Ahora mostramos por consola los resultados obtenidos
print(f"La suma de ambos numeros es: {suma}")
print(f"El resultado de la multiplicacion es: {producto}")
print("")
print("Fin del programa")