'''
    Ejercicio 4.->
        Realizar la carga de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar(Se ingresa un valor entero en el precio del producto)
'''
# Solicitamos los datos al Usuario en este caso de producto y cantidad, ambos de tipo entero como nos indica la glosa

valor_producto = int(input("Favor indicar el valor del producto: "))
cantidad_producto = int(input("Favor indicar la cantidad a llevar del producto: "))

# Ahora generamos una variable llamada precio_total, la cual nos indicara mediante una multiplicacion el valor total de la compra

precio_total = valor_producto * cantidad_producto

# Ahora mediante la funcion print mostramos el valor de la compra
print(f"El valor total de la compra es: {precio_total}")