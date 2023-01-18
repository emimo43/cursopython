# Jerarquia de Operaciones

num1 = 100
num2 = 50
num3 = 25
num4 = 10

print(num1 + num2) # Suma
print(num1 + num2 * num3) # Suma y Multiplicacion, primero se hara la Multiplicacion
print((num1 + num2) * num3) # primero son los parentesis
print((num1 + num2) * num3 - num4)
print((num1 + num2) * (num3 - num4))
print((num1 + num2) * (num3 - num4) / (num1 - num4)) # No puede una division dar zero o dara error como el siguiente ->

'''
Traceback (most recent call last):
  File "c:\cursopython\achiroupython\2.Operadores Aritmeticos\JerarquiaOperaciones.py", line 13, in <module>
    print((num1 + num2) * (num3 - num4) / (num1 - num1)) # No puede una division dar zero o dara error como el siguiente 
->
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
ZeroDivisionError: division by zero
'''