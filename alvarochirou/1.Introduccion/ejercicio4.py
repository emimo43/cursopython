"""Ejercicio 4:
Problema:
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)"""

# Solicitamos los datos del usuario
cantidad = int(input("Favor ingresar la cantidad de productos que comprara: "))
precio= int(input("Favor ingresar el precio individual del producto a comprar: "))

# Ahora multiplicamos el precio unitario por la cantidad de articulos para calcular el total
total = cantidad * precio

# Ahora mostraremos por pantalla el precio total
print(f"El precio total a pagar por la compra es: {total}")