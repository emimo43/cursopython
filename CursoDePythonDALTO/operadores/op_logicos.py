# En esta clase veremos los operadores logicos

# AND
resultado = True & True # Devolver True
resultado2 = False & True # Devolver Falso
resultado3 = True & False # Devolver Falso
resultado4 = False & False # Devolver Falso

# OR
resultado5 = True | True # Devolver True
resultado6 = False | True # Devolver True
resultado7 = True | False # Devolver True
resultado8 = False | False # Devolver Falso

# NOT
resultado9 = not True # Devolver Falso
resultado10 = not False # Devolver True
resultado11 = not 2 > 29 # Devuelve True debido a que not y false es True

# Mostramos por consola
print(f"Resultado, {resultado}")
print(f"Resultado 2, {resultado2}")
print(f"Resultado 3, {resultado3}")
print(f"Resultado 4, {resultado4}")
print(f"Resultado 5, {resultado5}")
print(f"Resultado 6, {resultado6}")
print(f"Resultado 7, {resultado7}")
print(f"Resultado 8, {resultado8}")
print(f"Resultado 9, {resultado9}")
print(f"Resultado 10, {resultado10}")
print(f"Resultado 11, {resultado11}")