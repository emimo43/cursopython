# En esta clase veremos la funcion input, la cual permite ingresar datos por consola

# Declaramos la variable y solicitamos los datos al Usuario para que los ingrese por consola

nombre = input("Por favor introduzca su nombre: ")
# Mostramos en el nombre por consola
print(nombre)
print(f"El nombre de la Persona es: {nombre}")

'''
    Tambien se puede usar con saltos de linea, con el parametro \n es el que indica el salto de linea
    
'''
nombre = input("Favor introduzca su nombre:\n")
print(f"Su nombre es: {nombre}")