# En esta clase veremos los diferentes metodos que tenemos para trabajar con los strings
cadena1 = "Hola soy Dalto"
cadena2 = "Bienvenido maquinola"

#print(dir(cadena1)) # El metodo dir nos muestra todos los metodos que tenemos para trabajar con los string, lo que si depende del objeto que tenga el string (numeros, textos, listas etc)

resultado = dir(cadena1)
print(resultado)

# Metodo upper() -> Convierte todo a mayuscula
resultado = cadena1.upper()
print(resultado)

# Metodo lower() -> Convierte todo a minuscula
resultado = cadena1.lower()
print(resultado)

# Metodo CAPITALIZE -> Convierte la primera en mayuscula, y el resto en minuscula
cadena3 = "hola soy Enrique"
resultado = cadena3.capitalize()
print(resultado)

# Metodo find() -> Metodo encuentra la primera aparicion del valor especificado, si no devuelve 1
# Buscamos una cadena en otra cadena, si no hay concidencia nos da -1
busqueda_find = cadena1.find("d")
print(busqueda_find) # Devuelve la posicion en que encuentra la cadena, si no encuentra nada nos devolvera -1

# Metodo index -> Buscamos una cadena en otra cadena -> Si no encuentra alguna coincidencia nos arroja una excepcion (error de codigo)
busqueda_index = cadena1.index("D")
print(busqueda_index)

# Metodo ISNUMERIC -> Si es numerico devuelve True si no devolvemos falso
es_numerico = cadena1.isnumeric()
print(es_numerico) # Nos retornara False (si fuera texto los numeros igual dara True por que el texto contiene numeros)

# Metodo ISALPHA -> Si es alfanumerico devuelve True, si no sera False, solo deben ser caracteres de la a - z no debe tener espacio ni caracteres especiales
es_alpha = cadena1.isalpha()
print(es_alpha) # Dara False por que solo es texto

# Metodo COUNT -> Devuelve el numero de ocurrencias de una subcadena en la cadena dada, devuelve la cantidad de veces que coincida, si no encuentra nada devuelve 0
contar_coincidencia = cadena1.count("Hola")
print(contar_coincidencia)


# Metodo LEN -> Cuenta los caracteres de una cadena, cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) # len() no es un metodo, es una funcion, va antes del argumento
print(contar_caracteres)

# Metodo STARTSWITH -> Verifica si una cadena comienza con
# Verificamos si una cadena empiza con otra cadena dada, si es asi devuele True
empieza_con = cadena1.startswith("H")
print(empieza_con)


# Metodo ENDSWITH-> Verifica si una cadena termina con
termina_con = cadena1.endswith("H") # Dara False
print(termina_con)

# Metodo REPLACE -> Reemplaza un valor por otro, reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Hola", "Holu Maquina") # El primer parametro es el que tiene, y el segundo por el que se reemplazara, si no encuentra coincidencias del primer parametro, devolvera la antigua cadena
print(cadena_nueva)
cadena_nueva2 = cadena_nueva.capitalize() # Dejaremos solo la primera letra con mayuscula con el metodo capitaliza()
print(cadena_nueva2)


# Metodo SPLIT -> Separa el parametro dado
# Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split() # Si no le ingreso datos como parametros me devuelve la lista separada en comas
print(cadena_separada) # Devolvera una lista