"""Problema:
    Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar(Se ingresa un valor entero en el precio del producto)"""

# Solicitamos los datos al usuario
precio = int(input("Favor ingresar el precio del producto: "))
cantidad = int(input("Favor ingresar la cantidad de productos a llevar: "))

# Operacion, multiplicamos el precio por la cantidad de productos para obtener el valor total
valorTotal = precio * cantidad

# Ahora mostramos por consola el valor total de la venta
print(f"El valor total de la compra es: {valorTotal}")