# Capitulo 3: Booleandos, condicionales y entrada de usuario.

# Entrada de datos del usuario. Identificacion del tipo de datos.

"""edad = input("Escribe tu edad por favor: ") # Aqui solicitamos los datos al usuario
tipo_de_datos = type(edad) # Aqui obtendremos a travez de la funcion type el tipo de dato de la variable edad
print(edad) # Mostramos por consola la respuesta
print(tipo_de_datos) # Mostramos por consola el tipo de dato de la variable tipo_de_datos"""

"""# BOOLEANOS, IF
verdadero = True
falso = False

if(verdadero == True):
    print("Soy verdadero !!!") # Cumple la condicion de verdadero

if(falso == True):
    print("Son iguales") # Esta condicion no se cumple por la cual no la vemos en consola

if(falso == False): # indicamos si false es igual a False, si esto se cumple, se imprimira el siguiente mensaje
    print("Si soy falso") # La condicion si se cumplio"""
# Operadores de Comparacion, elif, else

# Ejercicio -> Solicitamos la edad para poder pasar a la discoteque
"""edad = input("Dime tu edad por favor: ") # Solicitamos la edad, mediante la funcion input
edad = int(edad) # Aqui ingresamos un dato string pot input y con la funcion  int(edad) lo convertimos a int
if(edad >= 18): # Aqui indicamos si edad es mayor o igual a 18, si esto se cumple mostrara el siguiente mensaje
    print("Eres mayor de edad, puedes pasar")

elif(edad < 0): # Si la condicion del of no se cumple, salta a esta linea de codigo y consulta esta condicion
    print("Oye, esto es imposible")  

elif(edad < 14):
    print("Oye, eres muy pequeño")   

else: # La funcion else, se ejecutara si el if no es verdadero y mostrara el siguiente mensaje
    print("Eres menor de edad, no puedes pasar")    """

# Operadores Logicos and, or, not
# Usaremos el ejercicio de la edad para la discoteque

#Solicitamos los datos al usuario
"""edad = input("Dime tu edad, por favor: ")
edad = int(edad) # Convertimos la edad que viene como String a int"""

"""if(type(edad) == int): # Aqui consultamos si el tipo de la variable de edad es igual a entero
    if(edad > 120 or edad < 0):
        print("Esto no es posible")
    elif(edad >= 18 and edad < 40):
        print("Puedes entrar a mi club")
    elif(edad < 18 and edad > 15):
        print("Todavia eres un chaval, no puedes entrar")
    else:
        print("No ha sucedido ninguna de las condiciones")
else:
    print("Oye, que la edad debe ser un numero entero")  """

"""if (not(edad <= 18)): # Aqui estamos negando la condicion de la variable edad
    print("Puedes pasar") # Sin ingresamos la edad de 22 seria falso, pero la condicion not dira que es verdadera"""

"""
    Ejercicio -> Comprobar si el usuario introduce un numero, si no es un numero indicar que debe introducir un entero.
    Si es un numero, deberemos comprobar si es o no PAR, y notificarselo al usuario.
    Pistas -> isnumeric, num % 2 = 0
"""
# Solucion -> 
#  La funcion isnumeric solo funciona en cadena de texto, si el string contiene numeros nos devuelve TRUE en caso contrario False

"""texto = "hola"
txt = "22"
print(texto.isnumeric()) # isnumeric() es una funcion predeterminada de python
print(txt.isnumeric()) # Nos indica True por que es una cadena con numeros"""

# Solucion
"""num = input("Dime un numero: ")
if(not(num.isnumeric())):
    print("Datos incorrectos. Debe ser un numero")
else:
    num = int(num)
    if(num % 2 == 0):
        print("Es par")
    else:
        print("Es impar")  """

# Otra solucion, que es mejor en mi opinion
numero = input("Favor ingrese un numero entero: ")
#print(numero.isnumeric()) # Con el metodo isnumeric() sabemos si es numero o no
if(numero.isnumeric()): # Si la variable numero se complemente con metodo isnumeric, sigue la conicion
    numero = int(numero)
else:
    print("Debes introducir un numero entero")

if(type(numero) == int):
    if numero % 2 == 0:
        print("Es es un numero par")
    else:
        print("Es un numero impar")
"""else:
    print("Debes ingresar un numero entero") """      