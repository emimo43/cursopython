'''
Problema:
    Realizar un programa que solicite ingresar dos numeros distintos, y muestre por pantalla el mayor de ellos
'''
# Solicitamos los datos al Usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))

# Ahora generamos la condicion if para diferenciar cual es el numero mayor

if num1 > num2:
    print(f"El numero {num1} es mayor")
else:
    print(f"El numero {num2} es el mayor")
    
print("Fin del programa")        