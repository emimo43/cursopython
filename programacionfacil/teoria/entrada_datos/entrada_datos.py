# En esta clase veremos la entrada de datos por consola en Python, esto se hace con la funcion input

# Declaramos la variable y solicitamos los datos al Usuario para que este los ingrese
nombre = input("Por favor introduzca su nombre: ")
print(nombre)
print(f"El nombre es: {nombre}")

# Tambien se puede usar un salto de linea, con el parametro \n que es el que indica el salto de linea
nombre = input("Por favor introduzca su nombre\n")
print(f"Su nombre es: {nombre}")