""" Aplicacion IMC: Crear una aplicacion para calcular el IMC (indice de masa corporal)
IMC = peso/(Altura)*2 -> (altura) * (altura)
"""
# Solicitamos los datos al Usuario
print("Proporciona el peso:")
peso = input() # Ingresamos los datos por teclado
print("Proporciona el valor de la altura:")
altura = input()

# Ahora realizamos el calculo del IMC, debemos concatenar los valores como son string
imc = int(peso) / ((float(altura)) * (float(altura)))

# Ahora mostramos por consola el resultado de la operacion

print(f"Su IMC es:{imc}")