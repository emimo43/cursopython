'''
Ejercicio 4.- Problema:
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (Se ingresa un valor entero en el precio del producto)
'''
# Solicitamos los datos al Usuario
producto = int(input("Favor ingresar la cantidad de productos a llevar: "))
precio = int(input("Favor ingresar el precio del producto: "))

# Ahora generamos una variable llamada precio_total donde guardaremos el precio total y lo mostramos por consola
precio_total = producto * precio

print(f"El precio total de la venta es: {precio_total}")