# 1.-Imprime por pantalla el texto "Introduce el primer numero"
print("Introduce el primer numero: ")

# 2.-Crear la variable "dato1" con el primer valor introducido en el paso anterior
dato1 = input()

# 3.- Imprime por pantalla el texto "Introduce el segundo numero"
print("Introduce el segundo numero: ")

# 4.- Crear la variable "dato2" con el primer valor introducido en el paso anterior
dato2 = input()

# 5.- Convertir la variable "dato1" en una variable numerica denominada "numero1"
numero1 = int(dato1)

# 6.- Convertir la variable "dato2" en una variable numerica denominada "numero2"
numero2 = int(dato2)

# 7.- Crear la variable "suma" con la suma de "numero1" y numero2
suma = numero1 + numero2

# 8.- Convertir la variable "suma" en una variable de texto denominada "strSuma"
strSuma = str(suma)

# 9.- Crear la variable "resultado" con la concatenacion de "La suma es " y "strSuma"
resultado = "La suma es "+ strSuma

# 10.- Imprimir el valor de "resultado"
print(resultado)
print(type(resultado))