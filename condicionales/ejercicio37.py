# Ejemplo del uso del if, elif y else

# Ejercicio de condicional: 
# Comparar dos edades e indicar que edad es mayor, menor o igual con respecto a los datos
# Edad de Pedro y otra edad de Pablo

print("Escriba la edad de Pedro: ")
edadPedro = int(input())
print("Escriba la edad de Pablo: ")
edadPablo = int(input())

if edadPedro > edadPablo:
    print("La edad de Pedro es Mayor que la de Pablo")
elif edadPedro == edadPablo:
    print("Pedro y Pablo tienen edades iguales")
else:
    print("La edad de Pedro es menor que la de Pablo")        