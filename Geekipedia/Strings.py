# Esto es la Asignacion en Strings (+=)
print("Asignacion: ")
mensaje = "Hola"
mensaje += " "
mensaje += "Enrique"
print(mensaje)

# Esto es la concatenacion (+)
print("Concatenacion: ")
mensaje = "Hola"
espacio = " "
nombre = ("Enrique")
# Ahora vamos a concatenar con el simbolo +
print(mensaje + espacio + nombre)

# Casting
print("Casting -> Sirve para concatenar Str con numeros")
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos # Aqui sumamos las dos variables
resultado = str(resultado) # Aqui realizamos el casting de la variable resultado, el cual viene como numero entero y quedara como string
print("El resultado de la suma es: " + resultado)
# Ahora veremos una forma de imprimir con una variante del metodo format
print(f"El resultado de la suma es: {resultado}")

# La busqueda:
"""Consiste en localizar dentro de una cadena, una subcadena mas pequeña a un caracter.
    Para lo cual es necesario utilicar el metodo find"""
print("La busqueda: ")
mensaje = "Hola Enrique"
buscar_subcadena = mensaje.find("Enrique") # El metodo find nos permitira buscar la subcadena que necesitamos
print(buscar_subcadena) # Nos mostrara el numero de la subcadena gracias al metodo find

# La Extraccion:
"""Se trata de sacar fuera de una cadena, una porcion de la misma segun su posicion dentro de ella.
    Para ello es necesario indicar la posicion a extraer [1:8]"""
print("La extraccion: ")
mensaje = "Hola Enrique"
extraer_subcadena = mensaje[1:8] # Aqui estamos indicando que necesitamos extraer desde la posicion 1 hasta la 8, pero llega solo hasta la posicion 7
print(extraer_subcadena) # Mostramos por consola la subcadena que obtuvimos

# La comparacion:
"""Se utiliza para comparar dos cadenas de caracteres.
    Para ellos se utiliza el operador == """
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos) # Aqui nos mostrara si la comparacion es True o False
