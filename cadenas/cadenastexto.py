# Ahora veremos las cadenas de texto
# Declaramos una variable
cadena = "Hola mundo"
print(cadena)

# Para obtener el valor de una posicion en la cadena se recorre desde el 0 los espacios en blanco tambien se cuentan
print(cadena[5])
print(cadena[-1]) # Con este parametro estamos en la ultima posicion de la cadena
print(cadena[2:7]) # Al ingresar el ultimo parametro 7 nos mostrara hasta la posicion 6
print(cadena[2:]) # Aqui estamos mostrando desde la posicion 2 hasta el final

# No podificamos modificar los string solo consultarlo

cadena1 = "Hola"
cadena2 = "mundo"
cadena3 = " "

print(cadena1 + cadena3 + cadena2)
cadena = cadena1 + cadena3 + cadena2
print(cadena)