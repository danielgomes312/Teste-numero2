# O(n) time | O(n) space

# def sortedSquaredArray(array):
#     sortedSquareds = [0 for cada in array]
#     smallerValueIdx = 0
#     largerValueIdx = len(array) - 1

#     for idx in reversed(range(len(array))):
#         smallerValue = array[smallerValueIdx]
#         largerValue = array[largerValueIdx]

#         if abs(smallerValue) > abs(largerValue):
#             sortedSquareds[idx] = smallerValue * smallerValue
#             smallerValueIdx += 1
#         else:
#             sortedSquareds[idx] = largerValue * largerValue
#             largerValueIdx -= 1

#     sortedSquareds.sort()
#     return sortedSquareds

# array = [5, 12, 53, 6, 7, 23, 64, 73, 96]
# result = sortedSquaredArray(array)

# print(result)






# Define uma função chamada sortedSquaredArray que recebe uma lista chamada "array".
def sortedSquaredArray(array):
    # Cria uma nova lista chamada "sortedSquareds" com zeros, do mesmo tamanho da lista "array".
    sortedSquareds = [0 for cada in array]
    # Inicializa as variáveis para acompanhar os índices do valor menor e maior na lista "array".
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    # Itera pelos índices da lista "array" em ordem reversa.
    for idx in reversed(range(len(array))):
        # Obtém os valores menor e maior da lista "array" com base nos índices atuais.
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        # Compara os valores absolutos do valor menor e maior.
        if abs(smallerValue) > abs(largerValue):
            # Se o valor absoluto do valor menor for maior, armazena o quadrado do valor menor na lista "sortedSquareds".
            sortedSquareds[idx] = smallerValue * smallerValue
            # Atualiza o índice do valor menor para o próximo.
            smallerValueIdx += 1
        else:
            # Se o valor absoluto do valor maior for maior ou igual, armazena o quadrado do valor maior na lista "sortedSquareds".
            sortedSquareds[idx] = largerValue * largerValue
            # Atualiza o índice do valor maior para o próximo.
            largerValueIdx -= 1

    # Ordena a lista "sortedSquareds" em ordem crescente.
    sortedSquareds.sort()
    # Retorna a lista ordenada contendo os quadrados dos números.
    return sortedSquareds

# Lista de entrada.
array = [5, 12, 53, 6, 7, 23, 64, 73, 96]
# Chama a função sortedSquaredArray com a lista "array" e armazena o resultado em "result".
result = sortedSquaredArray(array)

# Imprime o resultado, que é a lista de quadrados ordenados.
print(result)






def sortedSquaredArray(array):
    # Cria uma lista para armazenar os quadrados dos valores em array.
    sortedSquareds = []

    # Inicializa dois ponteiros para os extremos da lista.
    # [5, 12, 53, 6, 7, 23, 64, 73, 96]
    #  ^   ^   ^  ^  ^   ^   ^   ^   ^
    #  |   |   |  |  |   |   |   |   |
    #  0   1   2  3  4   5   6   7   8
    # left                          right
    left, right = 0, len(array) - 1

    # Loop até que os ponteiros se encontrem.
    while left <= right:
        left_val, right_val = abs(array[left]), abs(array[right])

        # Compara os valores absolutos e adiciona o maior quadrado à lista.
        if left_val > right_val:
            sortedSquareds.insert(0, left_val ** 2)
            left += 1
        else:
            sortedSquareds.insert(0, right_val ** 2)
            right -= 1

    sortedSquareds.sort()
    return sortedSquareds

array = [5, 12, 53, 6, 7, 23, 64, 73, 96]
result = sortedSquaredArray(array)
print(result)