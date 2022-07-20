import prompt
import random


def run_even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
        elif number % 2 == 0 and user_answer != 'yes':
            print(f'''{user_answer} is wrong answer ;(. Correct answer was 'yes'
Let's try again,{name}!''')
            return()
        if number % 2 != 0 and user_answer == 'no':
            print('Correct!')
        elif number % 2 != 0 and user_answer != 'no':
            print(f'''{user_answer} is wrong answer ;(. Correct answer was 'no'
Let's try again,{name}!''')
            return()
        i += 1
    print(f'Congratulations, {name}')
    return()
