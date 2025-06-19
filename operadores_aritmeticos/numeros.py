# En esta clase veremos los tipos de datos numericos en Python, tenemos los tipos int y float

numero1 = 40
print(type(numero1)) # Con la funcion type podemos ver de que tipo de dato es la variable
print(numero1) # Ahora mostramos por consola el resultado de la variable

numero2 = 99.99
print(type(numero2))
print(numero2)

# Ahora veremos como convertir un tipo de dato int a float o viciversa

print(type(float(numero1))) # En este caso, numero1 es de tipo int y ahora cambia a tipo float
print(type(int(numero2))) # Ahora el tipo de dato float pasa a dato int