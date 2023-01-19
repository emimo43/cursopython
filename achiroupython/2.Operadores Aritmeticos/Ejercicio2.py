'''
Ejercicio 2 ->
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y 
la empresa de logística les cobra por peso de cada paquete, así que deben calcular el peso de los payasos y 
muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, realiza un programa que muestre el peso 
total de toda la venta.

Pista: Suponiendo que un cliente pide 5 payasos y 3 muñecas, la juguetería debería hacer la multiplicación 
de la cantidad de payasos con su peso, al igual que las muñecas; al tener ambos totales de peso, 
se debe sumar.

'''
# Primera forma de hacerlo segun el curso
print("El peso total es de: ", ((23 * 112) + (54 * 75)))

# Otra forma de hacerlo es con las variables y la cantidad en numero debido a que ese dato no cambia
compraPayasos = 23
compraMuñecas = 54

procedimiento = ((compraPayasos * 112) + (compraMuñecas * 75))
print(f"El peso total es de: {procedimiento}")


# Mi forma de hacerlo
pesoPayasos = 112
pesoMuñecas = 75
compraPayasos = 23
compraMuñecas = 54

cantidadPesoPayaso = 112 * 23
cantidadPesoMuñecas = 75 * 54

#print(cantidadPesoPayaso)
#print(cantidadPesoMuñecas)
totalPesoVenta = cantidadPesoPayaso + cantidadPesoMuñecas
print(f"El peso total es de: {totalPesoVenta}") # Lo hice perfecto -> Forma de concatenar

# Otra forma de concatenar es con la coma
print("El peso total es de: " , totalPesoVenta)