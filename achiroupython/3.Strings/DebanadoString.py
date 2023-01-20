# Veremos el Debanado de String
cadena = "Esto es un ejemplo de Substring (Debanado de Cadenas)"

print(len(cadena)) # El metodo len nos muestra la cantidad de caracteres que tiene la cadena
print(cadena[2]) # Con este metodo de [2] e indicando la posicion 2 me devuelve la letra t
print(cadena[50]) # Buscamos la posicion 50 del String, el cual es la letra a
print(cadena[0]) # Nos muestra la posicion 0 del String
print(cadena[7]) # Nos muestra un caracter blanco por que es un espacio

# El debanado indica que debemos indicar desde donde hasta donde mostraremos caracteres ejemplo:
print(cadena[0 : 11]) # El caracter de la derecha no se tomara en cuenta, en resumida en este caso mostrara del 0 al 10
print(cadena[ : 20]) # Nos mostrara desde el 0 al 19, si no le agrego nada al inicio
print(cadena[20 : ]) # Aqui me tomara desde el caracter 20 hasta el final
print(cadena[-1]) # Al colocar valores negativos, la cuenta comienza desde atras, en este caso parentesis al final
print(cadena[-0]) # El cero es neutro, no lo toma como negativo, lo que conlleva que me muestre la E como valor 0 inicial
print(cadena[-3]) # Nos muestra el 3 valor desde atras