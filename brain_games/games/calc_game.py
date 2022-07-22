import prompt
import random
from brain_games.main_logic import run_game


TASK = 'What is the result of the expression?'

def get_question_and_answer():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    ops = ['+', '-', '*']
    operator = random.choice(ops)
    question = (f'{number_one} {operator} {number_two}')
    answer = str(eval(str(number_one) + operator + str(number_two)))
    return (question, answer)

def run_calc_game():
    run_game(get_question_and_answer, TASK)
    return
    