#this is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
for guessTask in range(1, 7):
    print('take a task')
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break
    if guess == secretNumber:
        print('Good job, you guessed my number in ' + str(guessTask) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))