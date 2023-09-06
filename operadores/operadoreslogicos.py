# Veremos como esta el clima afuera, usaremos los operadores and y or
# Declaramos la variable
temperatura = int(input("¿Cual es la temperatura afuera? "))

# Generamos el ciclo
if temperatura >= 0 and temperatura <= 30: # Ambas condiciones deben ser verdaderas
    print(f"La temperatura esta bien hoy :D es de {temperatura} grados ")
elif temperatura < 0 or temperatura > 30: # Una de las condiciones debe ser verdadera
    print(f"La temperatura esta mal hoy :( es de {temperatura} grados")    

# EL operador not niega cualquier condicion    