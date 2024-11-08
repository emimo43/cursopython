'''
    Ejercicio 4 -> Problema -> Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
'''
# Solicitamos los datos al Usuario
precio = int(input("Favor ingrese el precio del producto: "))
producto = int(input("Favor ingresar la cantidad de productos a llevar: "))

# AHora multiplicamos el valor contra la cantidad y almacenamos este valor en una variable la cual contendra el valor total
precio_total = precio * producto

# Ahora mostramos en consola el resultado de nuestra venta
print(f"El precio total de la venta es: {precio_total}")