# En esta clase veremos en que consiste los operadores logicos es Python, los cuales son True o False

# Declaramos dos variables y las inicializamos con el valor True o False

a = True # la variable a contiene el valor verdadero o sea True
b = False # La variable b contiene el valor falso o sea False

# Operador and
# Ahora creamos la variable resultado en la cual vamos a comparar valores y obtendremos un valor booleando
resultado = a and b # Para que estas dos condiciones se cumplan deben ser verdaderas para que el print de True
print(resultado) # En este caso el resultado es false, debido a que las variables son diferentes

# Operador or
resultado = a or b # En este caso solo basta una variable que sea verdadera y nos da True
print(resultado) # En este caso nos da True

# Operador de negacion -> not
resultado = not a # En este caso nos debe dar el resultado de True --> Es un operador unario, solo necesita un valor
print(resultado) # Como la variable era True el negacion la cambio a false