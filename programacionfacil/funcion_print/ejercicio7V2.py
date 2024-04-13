'''
    Ejercicio 7 -> Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''

# Solicitamos los datos al Usuario
valor1 = float(input("Favor ingresar el primer valor: "))
valor2 = float(input("Favor ingresar el segundo valor: "))
valor3 = float(input("Favor ingresar el tercer valor: "))
valor4 = float(input("Favor ingresar el cuarto valor: "))

# Ahora generamos una funcion suma, la cual almacenara este valor
suma = valor1 + valor2 + valor3 + valor4

# Ahora creamos la funcion promedio, la cual almacenara esta operacion
promedio = suma / 4

# Ahora mostramos por consola el resultado
print(f"El valor de la suma es: {suma}, y el promedio es: {promedio}")