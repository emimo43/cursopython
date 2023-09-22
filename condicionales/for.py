# for -> iterar una seccuencia de elementos

colores = ["rojo", "verde", "azul"] # Esto es una lista de elementos

for color in colores: # Para la variable color en la lista de colores
    print(color) # Mostrara los elementos de uno en uno

# Ahora crearemos una cadena de caracteres
cadena = "Hola Mundo"
for caracter in cadena:
    print(caracter) # Mostraremos la cadena hacia abajo   

# Ahora veremos la funcion range que es rango
#range(8)
#print(range)
#print(range(0,8))  

for numero in range(8):
    print(numero)# Mostrara el numero hasta el 7 como el rango es de 8

for numero in range(3,8): # El rango sera desde el 3 hasta el 7
    print(numero)    

for numero in range(3,8,2): # El 2 es que indica que iremos de 2 en 2
    print(numero)    

# Ahora veremos la funcion break
for numero in range(10):
    if(numero == 5):
        break # El break se parara en el numero 5, mostrara desde el 0 al 4
    print(numero)    


# Ahora veremos la funcion continue, esto para la iteracion en el momento
# 
for numero in range(10):
    if(numero == 6):
        continue # Va a parar la iteracion en el 6 pero seguira al 7
    print(numero)  


# for doble -> sirve para recorrer matrices
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1, numero2)      