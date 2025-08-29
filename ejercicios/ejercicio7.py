'''
    Ejercicio 7.- Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''
# Solicitamos los datos al Usuario
valor1 = float(input("Favor ingrese el primer valor: "))
valor2 = float(input("Favor ingresar el segundo valor: "))
valor3 = float(input("Favor ingresar el tercer numero: "))
valor4 = float(input("Favor ingresar el cuarto numero: "))

# Calculamos en primer lugar la suma
suma = valor1 + valor2 + valor3 + valor4

# Ahora mostramos el valor de la suma por consola
print(f"El valor de la suma de los cuatro valores es: {suma}")

# Ahora realizamos el calculo del promedio

promedio = suma / 4

# Ahora mostramos por consola el resultado del promedio
print(f"El promedio obtenido es: {promedio}")