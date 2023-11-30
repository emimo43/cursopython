# Funcion print, permite imprimir en consola
print("Hola Mundo")
print("Mi nombre es Enrique")
# Ahora mostramos el salto de linea con la funcion \n
print("Hola Mundo\nMi nombre es Enrique")

# Video 4: Disposicion e valores (Variables)
# Creamos las variables
# Variables numericas
numero = 10 # tipo de dato int
print(numero) # Mostraremos por consola el valor de la variable
print(type(numero)) # La funcion type muestra el tipo de dato que contiene la variable

numero2 = 10.56 # tipo de dato float
print(numero2)
print(type(numero2))

# Tipo de dato Str (String)
cadena = 'a' # Tipo de dato str (String)
print(cadena)
print(type(cadena))

cadena2 = "Estoy 'estudiando" # Tipo de dato str (String)
print(cadena2)
print(type(cadena2))

# Tipo de datos Booleanos
valor = True
print(valor)
print(type(valor))

valor2 = False
print(valor2)
print(type(valor2))

# Operaciones con variables
num1 = 10
num2 = 6.7
suma = num1 + num2
print(suma)
print(type(suma))

num1 = 10
num2 = 6.7
suma = num1 + num2 * 10 / 6 # Python usa jerarquia de operaciones
print(suma)
print(type(suma))

num1 = 10
num2 = 6.7
resultado = (num1 + num2) * 10 / 6 # Python usa jerarquia de operaciones, ahora usamos parentesis para diferenciar la jerarquia
resultado = round(resultado,2) # Dejamos solo dos decimales
print(resultado)
print(type(resultado))
print("El resultado es:",resultado)
print(f"El resultado es: {resultado}")

# Ahora veremos que es lo que significa el tipado dinamico en Python, que es que la variable puede cambiar de valor incluso de tipo de dato
valor = 10
print(valor)

valor = "Enrique"
print(valor)

# Video 5: Comentarios.
valor = 10
print(valor)
print(type(valor))
valor = "Enrique"
print(valor)
print(type(valor))

# Python permite el tipado dinamico

'''
    El tipado dinamico es que una misma variable puede contener diferentes tipos
    de datos a lo largo del programa
'''