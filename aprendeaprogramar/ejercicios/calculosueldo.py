# Calcular el sueldo de un operario conociendo la cantidad de horas trabajadas y el pago por hora

# Solicitamos los datos al usuario
horasTrabajadas = float(input("Favor ingrese la cantidad de horas trabajadas: "))
pagoHora = float(input("Favor ingresar el pago por hora: "))

# Ahora crearemos una variable llamada sueldo que sera float para el calculo de este
sueldo = horasTrabajadas * pagoHora

# Ahora mostramos por consola el sueldo
# Ademas mostraremos de que tipo de dato es la variable sueldo
print(type(sueldo))
print(f"El sueldo del trabajador es: {sueldo}")