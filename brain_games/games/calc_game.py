import random
from brain_games.engine import run_game


GAME_DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = (f'{number_one} {operator} {number_two}')
    answer = str(eval(str(number_one) + operator + str(number_two)))
    return (question, answer)


def run_calc_game():
    run_game(get_question_and_answer, GAME_DESCRIPTION)
    return
