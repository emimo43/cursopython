# En esta clase veremos los operadores logicos (and, or, not)
numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8

print(numero1 > numero2) # True
print(numero3 < numero4) # True

# Ahora usaremos la condicion and donde estas deben ser todas verdadera
print((numero1 > numero2) and (numero3 < numero4)) # Dara como resultado True

print(numero3 > numero4) # False

print((numero1 > numero2) and (numero3 > numero4)) # Dara False, debido a que una condicion es false

# Ahora veremos el operador or, solo con una condicion verdadera el resultado sera verdadero
print((numero1 > numero2) or (numero3 > numero4)) # Dara True, debido a que una condicion es verdadera

# Ahora veremos el operador not(negacion)
print(numero3 > numero4)
print(not(numero3 > numero4)) # Al negar dira True