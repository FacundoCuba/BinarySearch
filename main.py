import random

def busquedaBinaria(lista, n):
    lista.sort()
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        medio = (minimo + maximo)//2
        if lista[medio] == n:
            return print(f"{n} esta en la lista")
        else:
            if lista[medio] < n:
                minimo = medio
            elif lista[medio] > n:
                maximo = medio
            else:
                print("Su numero no esta en la lista.")

if __name__ == "__main__":
    l = []
    c = int(input("Ingrese el tamaño de la lista: "))
    v = [None] * c
    for i in v:
        l.append(random.randint(0, 99))
    print(l)
    busquedaBinaria(l, int(input("Que numero desea buscar?: ")))