# En esta clase veremos la funcion condicional match, la cual es muy similar a la condicional if, muy similar a la funcion switch case de otros lenguajes como Java

numero = 3 # Creamos la variable numero, la cual almacena el numero 3

match numero: # Ahora con la condicion match veremos las condiciones
    case 1:
        print("Uno")
    case 2 :
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Numero no reconocido")            