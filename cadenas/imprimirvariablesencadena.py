# Ahora vermos como imprimir variables en las cadenas
nombre = "Antonio"
print("Buenos dias " + nombre) # Aqui estamos concatenando
print(f"Buenos dias {nombre}")

# El punto format
nombre = "Antonio"
edad = 18
print("Buenos dias {}, feliz {} cumpleaños".format(nombre,edad))

resultado = 10 / 3
print(resultado)
print("El resultado es {r}".format(r = resultado)) # Aqui formateamos usando la r
# Para acortar el resultado de los decimales usamos la siguiente formula
print("EL resultado es {r:1.3f}".format(r = resultado))
# En esta expresion estamos indicando que r:1 -> Es un entero .3 con 3 decimales

# Funcion f-strings
nombre = "Antonio"
edad = 18
print(f"Buenos dias {nombre},feliz {edad} cumpleaños")