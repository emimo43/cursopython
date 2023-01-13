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
edad = input("Dime tu edad por favor: ") # Solicitamos la edad, mediante la funcion input
edad = int(edad) # Aqui ingresamos un dato string pot input y con la funcion  int(edad) lo convertimos a int
if(edad >= 18): # Aqui indicamos si edad es mayor o igual a 18, si esto se cumple mostrara el siguiente mensaje
    print("Eres mayor de edad, puedes pasar")

# Operadores Logicos and, or, not