"""
Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal
"""
#  Solicitamos los datos al Usuario

letra = input("Favor ingrese una letra: ")
# Ingresamos a la condicion
if letra.lower() == "a":
    print("Es vocal")
elif letra.lower() == "e":
    print("Es vocal")  
elif letra.lower() == "i":
    print("Es vocal")
elif letra.lower() == "o":
    print("Es vocal")
elif letra.lower() == "u":
    print("Es vocal")
else:
    print("No es vocal")

    # Tambien se podia hacer con un ciclo anidado

"""Esta es una forma diferente y mas eficiente de hacerlo:

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("NO es una vocal")
"""    