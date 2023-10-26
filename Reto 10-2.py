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
    