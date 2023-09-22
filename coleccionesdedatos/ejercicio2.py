# Ejercicio 2:

# 1.- Crear una variable "tupla" que sea una tupla de los siguientes nombres: Antonio,Pedro y Maria
tupla =("Antonio","Pedro","Maria")

# 2.- Mostrar el valor de la variable "tupla"
print(tupla)
print(type(tupla))

# 3.- Recoger un dato por teclado y almacenarlo en la variable "dato"
print("Favor ingresar el dato solicitado")
dato = input()

# 4.- Si el valor de "dato" esta dentro de los valores de la variable "tupla" mostrar "Si"
if(dato in tupla):
    print(f"El dato {dato}'Si' esta en la tupla")

# 5.- Si el valor de "dato" no esta dentro de los valores de la variable "tupla", mostrar "No"
if(dato not in tupla):
    print(f"El dato {dato} 'No' esta en la tupla")