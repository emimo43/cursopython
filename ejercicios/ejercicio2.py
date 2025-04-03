'''
    Ejercicio 2.->
    
        Hallar la superficie de un cuadrado conociendo el valor de un lado
        
        La formula es superficie = lado * lado
'''
# Lo primero es solicitar los datos al Usuario

lado = int(input("Favor ingrese el valor del lado del cuadrado: "))

# Ahora creamos la formula de la solucion

superficie = lado * lado

# Ahora generamos la salida con la funcion print
print(f"La superficie del cuadrado es: {superficie}")