# while -> Un conjunto de accion mientras sean veridicas las condiciones

valor = 1
fin = 10

while(valor < fin): # Mientras valor sea menor que fin
    print(valor) # Se imprime valor
    valor = valor + 1 # El valor se incrementa en 1, se mostrara desde el 1 al 9


# Condicion while con funcion break
valor = 1
fin = 10

while(valor < fin):
    print(valor)
    valor = valor + 1
    if(valor == 5):
        break # Aqui finaliza el bucle, mostrara del 1 hasta el valor 4


# Condicion While con funcion continue 
valor = 1
fin = 10

while(valor < fin):
    valor = valor + 1
    if(valor == 6):
        continue
    print(valor)   