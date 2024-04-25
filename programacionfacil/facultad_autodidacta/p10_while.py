''' En esta clase veremos la estructura while'''

# Si hacemos el siguiente codigo sera un bloque infinito, debido a que no esta la condicion que lo detenga

'''
while True:
    print(Seccion de codigo)
'''

'''
    Esto crea un bloque de codigo infinito, nada lo detiene -> en vs code se detiene con ctrl + c para detenerlo
'''

# Creamos una variable contador
contador = 0 # Esta variable comienza en 0
while contador < 5: # Consultamos si contador es menor que 5
    print(f"El contador es: {contador}") # Mostramos por consola    
    contador = contador + 1 # Aqui incrementamos la variable contador
    
print(" ")    
    
contador = 1 # Esta variable comienza en 1
while contador < 5: # Consultamos si contador es menor que 5
    print(f"El contador es: {contador}") # Mostramos por consola    
    contador = contador + 1 # Aqui incrementamos la variable contador 
    
print(" ")       
    
contador = 1 # Esta variable comienza en 1
while contador < 6: # Consultamos si contador es menor que 6
    print(f"El contador es: {contador}") # Mostramos por consola    
    contador = contador + 1 # Aqui incrementamos la variable contador   
    
print(" ")     
contador = 1 # Esta variable comienza en 1
while contador < 11: # Consultamos si contador es menor que 11 -> Asi mostramos del 1 al 10
    print(f"El contador es: {contador}") # Mostramos por consola    
    contador = contador + 1 # Aqui incrementamos la variable contador