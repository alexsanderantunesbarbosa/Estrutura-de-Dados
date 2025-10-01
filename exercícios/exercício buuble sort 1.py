def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

# Exemplo de uso
minha_lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubble_sort(minha_lista)
print(lista_ordenada) 