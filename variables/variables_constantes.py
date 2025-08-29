'''
    En esta clase veremos las diferecias entre las constantes y las variables en el lenguaje de programacion python.
    Las constantes no existen en Python.
    Las variables como su nombre lo dicen varian en el flujo del programa
'''
cantidad_personas = 100
print(cantidad_personas)
cantidad_personas = 150
print(cantidad_personas)
cantidad_personas = 170
print(cantidad_personas)

# Para que una variable sea una constante, esta debe ser escrita en mayuscula
pi = 3.14
print(pi)
# En este caso esto no se toma como constante debido a que esta en minuscula

pi = 6.28
print(pi)

# Ahora generamos una variable en mayuscula para que esta sea una constante en Python
PI = 3.14
print(PI)

# Ahora si Yo cambio este valor igual lo hara, solo es una convencion entre desarrolladores
PI = 6.28
print(PI)