"""Ejrcicio 2: 
Problema: Hallar la superficie de un cuadrado conociendo el valor de un lado."""

# Solicitamos los datos al usuario
lado = input("Ingrese la medida del lado del cuadrado: ") # La funcion input nos permite ingresar datos por teclado
lado = int(lado) # Con la funcion int, convertimos el tipo de dato String a int
superficie = lado * lado # Aqui creamos la operacion que nos solicitan
print("La superficie del cuadrado es: ")
print(superficie) # Aqui mostramos por consola
# Esta es otra forma de mostrar por consola
print(f"La superficie del cuadrado es: {superficie}")