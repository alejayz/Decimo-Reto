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