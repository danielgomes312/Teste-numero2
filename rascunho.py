

# array = [-5, -14*1, -59, 12, 20, -23, 50, -121]

# valor1 = abs(array[1])
# print(valor1)

# left, right = 0, len(array) - 1

# print(left)
# print(right)

import random

number1 = random.randint(1, 1)
number2 = random.randint(1, 5)
number_of_guesses = 0

while number_of_guesses < 5:
    print('guess a number between 1 and 20: ')
    guess1 = input()
    guess1 = int(guess1)
    print('guess another number between 1 and 20: ')
    guess2 = input()
    guess2 = int(guess2)
    number_of_guesses += 1

    if guess1 == number1 and guess2 == number2:
        break
    elif number_of_guesses == 1:
        break
    else:
        print('Nope! try again.')

if guess1 == number1 and guess2 == number2:
    print('Correct! You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the numbers. The numbers was ' + str(number1) + ' - ' + str(number2))