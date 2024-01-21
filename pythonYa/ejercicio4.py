'''Problema: Realizar la carga del producto y la cantidad a llevar. Mostrar cuanto se debe pagar(Se ingresa un valor entero en el precio del producto)'''

# Solicitamos los datos al Usuario
cantidad = int(input("Favor ingrese la cantidad del producto a llevar: "))
precio_producto = int(input("Favor ingresar el precio del producto a llevar: "))

# Ahora generamos una variable la cual contendra el precio total del producto
precio_total = cantidad * precio_producto

# Ahora mostramos por consola el resultado de la operacion
print(f"El precio total a cancelar por el producto es: {precio_total}")