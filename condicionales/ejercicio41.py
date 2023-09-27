# Ejemplo de ejercicio con while

# Realiza una aplicacion que le pida al usuario una cantidad determinada de numeros
# Muestre al usuario tdodos los numeros impares que existen en la longitud proporcionada

print("Proporcione la longitud de numeros a evaluar: ")
cantidad = int(input())
numero = 1
print("Los siguientes numeros son impares: ")
while numero < cantidad:
    if((numero % 2)!= 0): # Debe ser diferente a 0, para que sea impar
        print(numero)
    numero += 1    