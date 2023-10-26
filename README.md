# Decimo-Reto

Para este repo tenemos como reto:

**1.** Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
def reales(lista: list)-> int:  # la entrada de la función es una lista
    suma = 0  #inicia la suma en cero
    for i in lista:
        suma += i #suma todos los elementos de la lista
    return suma / len(lista) # divide la suma entre el total de elememtos para hallar el promedio

if __name__ == "__main__":
    i = int(input("ingresar la cantidad de elementos para la lista: "))
    lista = [int(input("ingrese un número: ")) for x in range(i)]
    promArreglo = reales(lista) # se evalúa la función en los valores ingresados
    print("el promedio de " + str(lista) + " es: " + str(promArreglo))
```

**2.** Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```python
def productoPunto(listaA:list, listaB:list) -> int: # las entradas de la función serán las dos listas de numeros enteros
    producto = 0 #la variable que suma los datos de los productos, inicia en 0
    for i in range(len(listaA)): #verifica la cantidad de elementos de solo una de las listas dado que ambas tienen la misma cantidad.
        producto += listaA[i]*listaB[i] #calcula el producto de los elementos que estén en la misma posición en cada lista y suma los productos
    return producto

if __name__ == "__main__":
    n = int(input("ingrese la cantidad de elementos para ambas listas: "))
    listaA = [int(input("ingrese un número A: ")) for x in range(n)]
    listaB = [int(input("ingrese un número B: ")) for x in range(n)]
    proPunto = productoPunto(listaA, listaB)
    print("A = " + str(listaA))
    print("B = " + str(listaB))
    print("El producto punto de A y B es: " + str(proPunto))
```

**3.** Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
def ceros(lista: list) -> list: #la entrada de la función es una lista
    for i in range(len(lista)): #recorre los elementos de la lista
        if lista[i] == 0: #condición para identificar los ceros de la lista
            lista.pop(i) #elimina los ceros que encuentre en la lista
            lista.append(0) #agrega al final de la lista los ceros eliminados anteriormente
            
    return lista

if __name__ == "__main__":
    n = int(input("ingrese la cantidad de elementos para la lista: "))
    lista = [int(input("ingrese un número: ")) for x in range(n)]
    totalCeros = ceros(lista)
    print(lista)
```

**4.** Revisar que son los algoritmos de *sorting*, entender *bubble-sort*.

**Algoritmo de *sorting*:**
Un algoritmo de sorting, también conocido como algoritmo de ordenación es un conjunto de instrucciones que toman un arreglo o lista como entrada y organizan los elementos en un orden determinado. Las formas de ordenación pueden ser numéricas o de manetra de orden alfabético y pueden ser en orden ascendente (AZ, 0-9) o descendente (ZA, 9-0).

Los tipos de algoritmos de ordenación más comunes son:

Ordenamiento de burbuja (Bubble Sort): compara elementos en pares hasta que los elementos más grandes “burbujean” hasta el final de la lista y los más pequeños permanecen al principio.

Orden de selección (Selectión Sort): separa la lista en dos partes, ordenada y no ordenada, y “elimina” el elemento más pequeño de la parte sin ordenar y lo agrega a la parte ordenada.

Tipo de inserción (Insert Sort): separa la lista en dos partes, ordenadas y no ordenada. Se supone que el primer elemento está ordenado, luego el siguiente elemento se compara ese elemento con el primero, si es mayor, se queda como está pero si es más pequeño, se copea el primer elemento en la segunda posición y se inserta el segundo como primero.

Combinar ordenación (Merge Sort): divide la lista en dos, luego estas en 4 y así sucesivamente hasta que se formen listas de un elemento de longitud. Después, estos elementos se vuelven a unir en orden. 

Fuente: https://eiposgrados.com/blog-python/tipos-de-algoritmos-de-ordenacion-en-python/
