# En esta clase veremos funciones matematicas, primero importaremos la biblioteca math con la funcion import
import math # Importamos la liberia math
PI = 3.14
#print(round(PI)) # La funcion round que esta en la biblioteca math, nos redondea la variable, lo redondea a 3
# Para redondear un numero hacia arriba debemos usar la funcion ceil() -> de la siguiente manera math.ceil()
#print(math.ceil(PI)) # Lo redeondea a 4
# Para redondear el numero hacia abajo usamos la funcion floor() -> En este caso de la siguiente manera math.floor()
#print(math.floor(PI)) # En este caso sera 3
# La funcion absoluta se usa de la siguiente manera(abs()) -> en el siguiente ejemplo si dejamos PI con valor negativo, nos dara un valor positivo
#print(abs(PI))
# La funcion pow (potencia)nos eleva un numero, en este caso se ingresa la base y el exponente como el siguiente ejemplo
#print(pow(PI,2))
# La funcion sqrt (math.sqrt()) nos permite obtener la raiz cuadrada
#print(math.sqrt(420))

# Ahora veremos como hacer el maximo y minimo
x = 2
y = 1
z = 3
print(max(x,y,z)) # Nos dara el valor maximo
print(min(x,y,z)) # Nos dara el valor minimo
