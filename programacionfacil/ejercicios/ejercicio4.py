'''
    Problema -> Ejercicio 4 -> Realizar la carga del producto de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (Se ingresa un valor entero en el precio del producto)
'''

# Solicitamos los datos al Usuario
producto = int(input("Favor ingresar la cantidad de producto a llevar: "))
precio = int(input("Favor ingresar el valor del producto: "))

# Ahora generamos una variable para obtener el valor total de la compra
precio_total = producto * precio

# Ahora mostramos por consola el valor del producto total
print(f" El valor total de la compra es: {precio_total}")