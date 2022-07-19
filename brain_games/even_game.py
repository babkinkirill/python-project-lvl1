import prompt
import random


    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

def run_even_game():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    user_answer = prompt.string(f'Your answer: ')
    if number % 2 == 0 and user_answer == 'yes':
        print('Correct!')
    if number % 2 != 0 and user_answer == 'no':
        print('Correct')
        return()
    print(f"Wrong answer.\nLet's try again, {name}!")
 


