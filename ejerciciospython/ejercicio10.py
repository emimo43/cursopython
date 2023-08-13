# Solicitar valores al usuario

# Solicitamos datos al usuario
print("Deme un valor 1")
a = input()
print("Deme un valor 2")
b = input() # Ingresamos los datos por el usuario

# Los datos ingresados por el usuario entran como string(cadena de texto)

c = int(a) + int(b) # Aqui estamos casteando los valores ingresados por teclado a numeros entero con la funcion int

# Ahora mostramos por consola el resultado de la operacion
print("La suma de los valores es:",c) # Concatenamos el texto con una coma para mostrar el valor de la variable
