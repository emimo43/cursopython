# En esta clase veremos la entrada de datos por teclado
# Declaramos las variables, solicitando los datos al Usuario

palabra = input("Introduce una palabra: ")
num_int = int(input("Introduce un numero entero: ")) # Convertimos el str ingresado a entero
num_float = float(input("Introduce un numero floatante: ")) # Convertimos el str ingresado a flotante
num_compless = complex(input("Introduce un numero complejo: ")) # Convertimos el str ingresado a numero complejo para la salida en consola

# Mostramos los datos por pantalla
print(f"String: {palabra}")
print(f"Entero: {num_int}")
print(f"Flotante: {num_float}")
print(f"Numero complejo: {num_compless}")
                  
              
              
