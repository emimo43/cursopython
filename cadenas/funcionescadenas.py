# Ahora veremos las funciones de las cadenas
cadena = "Hola Mundo"
print(cadena)
print(len(cadena))#El metodo len nos indica cuantos caracteres tiene mi cadena

# Para convertir una cadena a mayuscula usamos el metodo upper
cadena2 = cadena.upper()
print(cadena2)
print(cadena)
print(cadena.upper())#Aqui solo mostramos imprimiendo en consola a mayuscula
print(cadena)

# Para poner una cadena en minuscula usamos la funcion lower()
cadena3 = cadena.lower()
print(cadena3)
print(cadena.lower())
print(cadena)

# El metodo split() nos muestra la lista que tiene la cadena (divide la cadena) devuelve una lista de nuestra cadena
cadena4 = cadena.split()
print(cadena4)
print(cadena.split())
print(cadena)

# Ejemplo de split
cadena5 = "uva,pera,manzana,naranja"
print(cadena5)
# Si quieremos dividir con el metodo split() usaremos la coma como parametro y la debemos usar entre comillas
cadena5 = cadena5.split(",")
# Ahora la mostramos por consola
print(cadena5)

