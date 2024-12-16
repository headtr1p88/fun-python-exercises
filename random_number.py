#Write a number guessing game where the user has to guess a number from 1-10
#The user has three guesses
#If the user guesses incorrectly, advise the user if the guess was too high or low
import random

random_number = random.randint(1,10)
user_guess = int(input('Guess a number from 1 to 10: '))
user_attempts = 1

while True:
    if user_guess == random_number:
        print(f'Congrats, you guessed the number {random_number} in {user_attempts} attempt(s)')
        break
    else:
        if user_attempts == 3:
            print(f'Bad luck! The number was {random_number}')
            break
        if user_guess > random_number:
            user_guess = int(input('Your guess was too high! Try again: '))
        else:
            user_guess = int(input('Your guess was too low! Try again: '))
        user_attempts += 1