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