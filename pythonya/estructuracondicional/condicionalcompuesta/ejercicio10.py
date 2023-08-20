"""Problema: Realizar un programa que solicite ingresar dos numeros distintos, y muestre por pantalla el mayor de ellos"""

# Solicitamos los datos al usuario, donde casteamos enseguida el str a int
num1 = int(input("Favor ingrese el primer numero: "))
num2 = int(input("Favor ingrese el segundo numero: "))

# Ahora realizamos el ciclo if para ver la condicion
if(num1 > num2):
    print(f"El {num1} es mayor que el {num2}")
else:
    print(f"El {num2} es mayor que el {num1}")