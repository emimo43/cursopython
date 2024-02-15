'''
Problema:
    Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''
# Solicitamos los datos al Usuario, sera de tipo float
nota1 = float(input("Favor ingrese la primera nota: "))
nota2 = float(input("Favor ingresa la segunda nota: "))
nota3 = float(input("Favor ingresa la tercera nota: "))
nota4 = float(input("Favor ingresa la cuarta nota: "))

# Ahora generamos la variable promedio para obtener el resultado necesario
suma = nota1 + nota2 + nota3 + nota4
promedio = suma / 4

# Ahora mostramos por consola el valor obtenido
print(f"El promedio de las cuatro notas es: {promedio}")
print("")
print("Fin del programa")