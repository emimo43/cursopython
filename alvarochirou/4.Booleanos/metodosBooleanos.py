# En esta clase veremos los metodos booleanos.

cadena = "Estoy mostrando los metodos booleanos para las Strings"
cadena2 = "CMSJDNCFISDNFISDNCINXICNDIUNSIJND"
cadena3 = "cmindcvndsifdnfijofnisncnsmed"

print(cadena.startswith("e")) # Este metodo verifica si con el parametro que le asigno esta en la cadena, en este caso dara False por que la e es en minuscula
print(cadena.endswith("S")) # Este metodo es la contra parte del primero, ve como finaliza la cadena, en este caso es una S mayuscula por lo cual es False

print(cadena2.isupper()) # Verifica si todo esta en mayuscula, o sea es True
print(cadena3.islower()) # Verifica si todo esta en minuscula por lo cual es True