

def isValidSubsequence(array, sequence):
    # o inicio da contagem usando o numero de objetos dentro do array len(array)
    j = 0
    #iniciando o loop
    for i in range(len(array)):
        # se o nomero apontado do array for igual o numero da sequencia.
        if array[i] == sequence[j]:
            #então vai pular para o proximo numero do array.
            j += 1
            # agora se todos os numeros apontados foram encontrados no Array retornar True
            if j == len(sequence):
                # caso todos os numeros apontados foram iguais foram iguais.
                return True
    # caso algum dos numeros apontados pelo i não for encontrado mandar False.
    return False
    pass

array = [5, 1, 22, 25, 6, -1, 8, 10]
#lenn = [0, 1,  2,  3, 4,  5, 6,  7]

sequence = [1, 6, -1, 10, 7]


result = isValidSubsequence(array,sequence)
print(result)