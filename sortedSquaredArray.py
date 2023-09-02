# O(n) Space

def sortedSquaredArray(array):
    # Cria uma lista chamada sortedSquares preenchida com zeros, onde cada zero
    # corresponde a um elemento da lista de entrada "array".
    sortedSquares = [0 for cada in array]

    # Itera através dos índices da lista de entrada "array".
    for idx in range(len(array)):
        # Obtém o valor do elemento da lista de entrada no índice atual.
        value = array[idx]

        # Calcula o quadrado do valor e atribui o resultado ao elemento
        # correspondente na lista sortedSquares.
        sortedSquares[idx] = value * value

    # Ordena a lista sortedSquares em ordem crescente.
    sortedSquares.sort()

    # Retorna a lista de quadrados ordenada.
    return sortedSquares

# Lista de entrada
array = [10, -4, 3, 29, 5, 6, 7, 8, 9]

# Chama a função sortedSquaredArray com a lista de entrada e armazena o resultado em "result".
result = sortedSquaredArray(array)
print(result)