# En esta clase veremos la concatenacion
'''
    Algo que vamos a necesitar al trabajar con string (texto) es la concatenacion. Esta se hace con el operador + y lo que hace es unir dos trozos de texto. Prueba ahora añadir una frase con el nombre
'''
nombre = input("Por favor introduzca su nombre: ")
print("Bienvenido/a " + nombre + ".") # Esta es la forma mas tradicional

# Ahora veremos la mas actual
nombre = input("Por favor introduzca su nombre: ")
print(f"Bienvenido/a {nombre}")