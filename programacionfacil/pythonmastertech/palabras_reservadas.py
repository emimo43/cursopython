'''
    Ver el listado de palabras reservadas de Python en la consola
    Algo muy práctico que puedes hacer, es escribir el siguiente código en un archivo de Python. Este pequeño código, lo que hace, es mostrar en la consola el listado de las palabras clave de Python.


'''
import keyword
print(keyword.kwlist) # Con este metodo nos muestra el listado de las palabras reservadas de Python

'''
    Palabras blandas
Algunas palabras son determinadas en la referencia oficial de Python, como soft keywords (palabras clave blandas).

Estas palabras son las siguientes:

match (versión 3.10)
case (versión 3.10)
type (versión 3.12)
_ (versión 3.10)
Lo que aparece entre paréntesis es la versión en la que se añadieron estas palabras blandas. Al ser bastante recientes, no podemos descartar que vaya a haber más, en un tiempo no muy lejano.

Estos identificadores están definidos en el propio lenguaje Python, pero no están reservados, por eso, no aparecen en el listado de palabras reservadas.

El motivo de que haya estas palabras blandas, es para establecer retrocompatibilidad. Con el tiempo, se van añadiendo estructuras nuevas, como la de match. Esto quiere decir, que es posible que mucho software anterior a esa versión, escrito con Python, utilice una palabra tan común como esta, que significa en español, “coincidencia”. Hay muchos programas antiguos que llevan variables o funciones, llamadas de esa forma.

En conclusión, la decisión de no forzar estas palabras, como palabras reservadas, fue una decisión tomada para permitir la migración de programas antiguos sin grandes cambios.

Con una palabra blanda puedes hacer esto, aunque no es recomendable:

match = 10

Pero con una palabra reservada, aunque quieras, no puedes hacer esto, recuerda el ejemplo de global del principio del capítulo.

'''