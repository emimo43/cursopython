# Capitulo 3: Booleanos, condicionales, y entrada de usuario.


# Entrada de datos del usuario. Identificacion del tipo de datos.
"""edad = input("Escribe tu edad por favor: ")#Solicitamos los datos al usuario
#print(edad)#Mostramos la edad
#Para ver que tipo de dato estamos usando, usamos la funcion type
typo_de_datos = type(edad)
print(edad)
print(typo_de_datos)#Aqui mostraremos que tipo de dato usamos"""


# BOOLEANOS, IF.
verdadero = True #Esto es un booleano
falso = False

if(verdadero == True):
    print("Soy verdadero!!!")

if(falso == True):#No se ejecutara por que no cumple la condicion
    print("Son iguales")    

if(falso == False):
    print("Si soy Falso")   

# Operadores de Comparacion, elif, else


# Operadores logicos and, or , not


# Ejercicio. Comprobar si el usuario introduce un numero, si no es un numero.

# Indicar que debe introducir un entero. Si es un numero, deberemos comprobar, si es o no PAR, y notificarselo al usuario