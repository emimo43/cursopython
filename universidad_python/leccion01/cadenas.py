# En esta clase veremos las cadenas (string)

# Cadena (String)
miGrupoFavorito = "Rainbow"
print(miGrupoFavorito)
print(type(miGrupoFavorito))
print("Mi Grupo Favorito es: " + miGrupoFavorito) # Concatenacion

miGrupoFavorito = "Rainbow" + " Best Rock Band" # Concatenacion
print(miGrupoFavorito)
print(type(miGrupoFavorito))
print("Mi Grupo Favorito es: " + miGrupoFavorito) # Concatenacion

miGrupoFavorito = "Helloween"
comentario = "The Best Rock Band"
print(miGrupoFavorito)
print(type(miGrupoFavorito))
print("Mi Grupo Favorito es: " + miGrupoFavorito + " " + comentario) # Concatenacion
print( " ")

# Otra manera de concatenar
print("Mi grupo favorito es:",miGrupoFavorito,comentario) 
print(" ")

numero1 = "1"
numero2 = "2"
print(numero1 + numero2) # Aqui no suma, concatena dos string
print(" ")
# Para que podamos sumar string, debemos usar el metodo int o float para convertir este dato en numerico
print(int(numero1)+ int(numero2))
print(" ")

numero1 = 1
numero2 = 2
print(numero1 + numero2) # Aqui esta sumando dos numeros enteros
print(" ")
