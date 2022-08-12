import random


def insertion_sort(lista):
    qtde_elementos = len(lista)
    for i in range(1, qtde_elementos):
        temp = lista[i] 
        j = i - 1 
        while j>=0 and lista[j] > temp:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = temp  
        



lista = [random.randrange(1, 45, 2) for i in range(31)]
print(lista)
insertion_sort(lista)
print(lista)