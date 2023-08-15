# Problema: Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar(Se ingresa un valor entero en el precio del producto)

# Solicitamos los datos al usuario:
print("Favor ingresar el valor del producto: ") # Ingresamos el valor como str
precio = int(input()) # Casteamos el valor a int, debido a que viene como str
print("Favor ingresar la cantidad a llevar del producto: ")
cantidad = int(input())

# Ahora realizamos la operacion para calcular el total de la compra
precio_total = precio * cantidad

# Ahora mostramos por consola el resultado total
print(f"El valor total de la compra es: {precio_total}")