# En este clase veremos el ciclo while, es una instruccion que solo se realizara mientras la condicion sea verdadera, debe tener una sentencia de detencion o se mantendra como condicion infinita

nombre = "" # La variable nombre esta vacia

while not nombre or len(nombre) == 0: # Alguna de estas dos condiciones debe ser verdadera
    nombre = input("Ingresa tu nombre: ")

print(f"Hola {nombre}")    