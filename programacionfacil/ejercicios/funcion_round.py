'''
    En esta clase veremos la funcion round en Python, la cual nos permite redondear un numero
'''

# Crearemos dos variables y obtendremos un resultado de una operacion

numero1 = 15.345
numero2 = 25.456

# Ahora creamos una multiplicacion
producto = numero1 * numero2

# Ahora mostramos por consola el resultado de esta operacion
print(f"El resultado de la multiplicacion de los numeros {numero1} con {numero2}, es: {producto}")

# Si nos fijamos, el resultado nos muestra 5 decimales, y solo lo necesitamos con 2, entonces ocuparemos la funcion round
print(" ")
producto = round(producto,2)

# Ahora volvemos a mostrar por consola el resultado
print(f"El resultado de la multiplicacion de los numeros {numero1} con {numero2}, es: {producto}")
