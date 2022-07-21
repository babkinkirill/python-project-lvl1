import prompt
import random


def run_calc_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    i = 1
    while i <= 3:
        number_one = random.randint(1, 100)
        number_two = random.randint(1, 100)
        ops = ['+', '-', '*']
        operator = random.choice(ops)
        result = eval(str(number_one) + operator + str(number_two))
        print(f'Question: {number_one} {operator} {number_two}')
        user_answer = int(prompt.string('Your answer: '))
        if result == user_answer:
            print('Correct!')
        else:
            print(f'''{user_answer} is wrong answer ;(. Correct answer was {result}
Let's try again,{name}!''')
            return()
        i += 1
    print(f'Congratulations, {name}!')
    return()