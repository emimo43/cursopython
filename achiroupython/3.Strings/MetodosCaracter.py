# Veremos los metodos de cadena
cadena = 'Estoy utilizando los metodos de Python' # Ojo con las tildes en Python, este lenguaje no se lleva bien con las tildes
cadena2 = "ESTOY UTILIZANDO LOS METODOS EN PYTHON"
cadena3 = 'estoy utilizando los metodos de Python'
cadena4 = 'Estoy utilIzando lOs metodos de Python'
print(cadena.lower()) # El metodo lower convierte las mayusculas en minusculas, siempre el metodo lo antecede un . y luego parentesis en este caso el metodo lo aplicamos a la variable cadena.lower()
print(cadena2.lower()) # Nos convertira toda esa cadena que tiene mayuscula a minuscula
print(cadena.upper()) # Con este metodo convertimos todas las minusculas en Mayusculas
print(cadena3.capitalize()) # El metodo capitalize() realiza la conversion a mayuscula de la primera letra del String, y las otras letras que estan en Mayuscula las convierte a minusculas, en resumen este metodo solo deja la primera letra en mayuscula del String
print(cadena3.title()) # Este metodo convierte todas las primeras palabras del String y las convierte a Mayusculas
print(cadena4.swapcase()) # Este metodo convierte las mayusculas a minusculas y las minusculas a mayusculas
