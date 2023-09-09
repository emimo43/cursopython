"""# El ciclo for se ejecuta un limitado numero de veces

# Ejemplo de un ciclo que cuenta desde 1 hasta 10
for x in range (1,11): # Se pone 11 en este caso debido a que la posicion 0 sera el numero 1
    print(x)

# Contar del 50 al 100
for x in range(50,101):
    print(x)  

# Para ir en un ciclo for contando de 2 en 2 se usa el pass
for x in range(50,101,2):
    print(x)      
"""
# Ahora realizaremos un programa de cuenta regresiva usando la funcion time
import time

for s in range(10, 0, -1):
    print(s)
    time.sleep(1) # El metodo sleep en este caso esperara 1 segundo para iterar

print("Feliz año nuevo!")    