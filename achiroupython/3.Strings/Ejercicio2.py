'''Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.
'''
cadena = "Separado"
print(cadena)
cadena = cadena.replace("Separado", "S,e,p,a,r,a,d,o") # Replace es el metodo con quien reemplazo el String original, siempre debe ser con variable
print(cadena)

# Esta es la forma mas practica para realizar el ejericio
palabra = "eparado"
palabraNew = palabra.replace("" , ",")
print("S",palabraNew)

# Me convence mas la forma en que yo hice el ejercicio