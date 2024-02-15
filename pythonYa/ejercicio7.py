'''
Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''
# Solicitamos los datos al Usuario
numero1 = float(input("Favor ingresar el primer numero: "))
numero2 = float(input("Favor ingresar el segundo numero: "))
numero3 = float(input("Favor ingresar el tercer numero: "))
numero4 = float(input("Favor ingresar el cuarto numero: "))

# Ahora creamos la variable suma y promedio, en la cual guardaremos los resultados
suma = numero1 + numero2 + numero3 + numero4
promedio = suma / 4

print(f"El valor de la suma de los cuatro numeros es: {suma}, y el promedio es: {promedio}")