# Ejercicio3

#1.- Crear una variable "numeros" con la lista de los numeros del uno al 10 (ambos incluidos)
numeros = [1,2,3,4,5,6,7,8,9,10]

# 2.- Mostrar el valor de la variable "numeros"
print(numeros)

# 3.- Recoger un dato del teclado y almacenarlo en la variable "dato"
print("Favor ingrese un numero")
dato = input()

# 4.- Convertir "dato" en numerico y almacenarlo en la variable "numero"
numero = int(dato)

# 5.- Si el valor "numero" esta en la lista de numeros, mostrar el mensaje "SI"
if(numero in numeros):
    print("SI")

# 6.- Si el numero introducido no esta en la lista de numeros, mostrar el mensaje "NO"
if(numero not in numeros):
    print("NO")