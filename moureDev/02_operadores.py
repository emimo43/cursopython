# En esta clase veremos los operadores
# Operadores Aritmeticos.

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Aqui vemos el modulo el coeciente de la division
print(10 // 3) # Esta es la division entera
print(2 ** 3) # Esta es la exponenciacion
print(2 ** 3 + 3 - 7 / 1 // 4) # Esta operacion lo vera por jerarquia el lenguaje Python

# Operaciones con cadenas de texto
print("Hola " + "Python " + "Que tal?") # Aqui concatenamos los str
print("Hola " + str(5)) # Con la funcion str() estamos convirtiendo el entero en str para poder concatenarlo para mostrarlo por pantalla

# Operaciones mixtas
print("Hola " * 5) # Con este metodo me mostrara 5 veces el mensaje Hola, indica que mostrara 5 veces el texto
print("Hola " * (2 ** 3)) # Aqui mostrara 8 veces el string, debido a que el 2 se eleva 3 veces

my_float = 2.5 * 2
print("Hola " * int(my_float)) # Mostrara 5 veces el mensaje hola, debido a que el int convierte la variable flotante en entero

# Operadores comparativos

# Operadores con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4) # Distinto a !=

# Operaciones con cadenas de texto
print("Hola" > "Python") # False
print("Hola" < "Python") # True
print("aaaa" >= "abaa") # Ordenacion alfabetica por ASCII, ve cual letra es mayor por el alfabeto
print(len("aaaa") >= len("abaa")) # Cuenta de caracteres, metodo len() ve la longitud de la cadena
print("Hola" <= "Python")
print("Hola" == "Hola") # True
print("Hola" != "Python") # True

# Operadores Logicos
# Basada en el algebra de Bole
print(3 > 4 and "Hola" > "Python") # False - False and False = False
print(3 > 4 or "Hola" > "Python") # False
print(3 < 4 and "Hola" < "Python") # True
print(3 < 4 or "Hola" > "Python") # True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True
print(not(3 > 4)) # True -> niega el resultado de la condicion


