'''
Problema:
    Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)
'''

# Solicitamos los datos al Usuario
lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora creamos una variable llamada perimetro, la cual contendra el mismo nombre
perimetro = lado * 4

# Ahora mostramos por pantalla el resultado de esta operacion
print(f"El valor del perimetro del cuadrado es: {perimetro}")