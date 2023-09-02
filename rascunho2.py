

# array = [-5, -14*1, -59, 12, 20, -23, 50, -121]

# valor1 = abs(array[1])
# print(valor1)

# left, right = 0, len(array) - 1

# print(left)
# print(right)

# import random

# number = random.randint(1, 25)
# number_of_guesses = 0

# while number_of_guesses < 5:
#     guess = int(input('Guess a number between 1 and 25: '))
#     number_of_guesses += 1

#     if guess == number:
#         print(f'Correct! You guessed the number in {number_of_guesses} tries!')
#         break
#     else:
#         print('Nope! Try again.')

# if number_of_guesses == 5 and guess != number:
#     print(f'You did not guess the number. The number was {number}.')

import random

# Gera dois números aleatórios entre 1 e 15 (inclusive)
number1 = random.randint(1, 15)
number2 = random.randint(1, 15)

# Imprime os números gerados
print("Número 1:", number1)
print("Número 2:", number2)