"""Se solicita incluir la siguiente informacion acerca de un libro:
titulo
autor
debes imprimir la informacion en el siguiente formato:
proporciona el titulo
proporciona el autor
<titulo> fue escrito por <autor>"""

# Declaramos las variables y solicitamos los datos al Usuario
print("Detalles de la solicitud de Libro: ")
titulo = input("Favor indicar el titulo del libro: ")
autor = input("Favor ingresar el autor del libro: ")

# Mostramos por consola lo solicitado
print(f"{titulo} fue escrito por {autor}")