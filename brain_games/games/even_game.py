import random
from brain_games.main_logic import run_game


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, answer)


def run_even_game():
    run_game(get_question_and_answer, TASK)
    return
