'''def saludo():
    print("Hola Carolina, tu puedes con esta 'mamada'")
    
saludo()    '''

# En esta clase veremos la funcion input() -> La cual nos permite realizar ingreso de datos por teclado (consola)

# input("Ingresa tu nombre: ")  # -> Aqui solicitamos el nombre al Usuario

# Recordar que todo lo que se ingresa con la funcion input() es un string o cadena de texto

'''nombre = input("Ingresa tu nombre: ")
print(nombre)'''

'''resultado = 0
a = 0
b = 3

a = int(input("Escribe un numero: ")) # Antes de la funcion input, debemos indicar que cambie el str a entero con la funcion int

resultado = a + b

print(resultado)'''

# Ahora veremos la conversion a tipo de dato float

a = float(input("Escribe un numero decimal: "))
b = 5.5
resultado = a + b
print(resultado)

# Ahora veremos la concatenacion entre str y otro tipo de dato
print("El resultado es: ", resultado) # Aqui nos concatena la ,(coma)
print("El resultado es: + str(resultado)") # Aqui convertimos el tipo de dato float con la funcion str()
# La ultima funcion que veremos y para mi la mejor es el f string
print(f"El resultado 2 es: {resultado}")