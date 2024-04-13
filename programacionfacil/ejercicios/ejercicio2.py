'''
    Ejercicio2 -> Problema --> Hallar la superficie de un cuadrado, conociendo el valor de un lado
    
    La formula es: superficie = lado * lado
'''

# Lo primero que debemos hacer es solicitar los datos al Usuario, con la funcion input, con la cual podemos ingresar los datos

lado = int(input("Favor ingrese el valor del lado del cuadrado: "))

# Ahora generamos la formula para obtener el resultado esperado

superficie = lado * lado

# Ahora mostramos por consola el resultado que obtenemos por consola
print(f"El valor de la superficie del cuadrado es: {superficie}")
