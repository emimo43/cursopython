# Problema: Hallar la superficie de un cuadrado conociendo el valor de un lado
# La formula para encontrar la superficie de un cuadrado es: superficie = lado * lado

# Solicitamos los fatos al usuario
print("Favor ingrese el valor del lado")
lado = int(input())

# Ahora realizamos la operacion, creando la variable superficie
superficie = lado * lado

# Ahora mostramos los datos por consola
print(f"El valor de la superficie del cuadrado es: {superficie}") # Esta es otra forma de concatenar la variable