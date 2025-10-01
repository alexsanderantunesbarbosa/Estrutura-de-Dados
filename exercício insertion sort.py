def insertion_sort(array):
    n=len(array)
    for i in range(1,n):
        marcado=array[i]
        j = i-1
        while j >= 0 and marcado < array[j]:
            array[j+1] = array[j]
            j = j-1
            array[j+1] = marcado
    return array

# Exemplo de uso
minha_lista = [12, 11, 13, 5, 6]
lista_ordenada = insertion_sort(minha_lista)
print(lista_ordenada) 