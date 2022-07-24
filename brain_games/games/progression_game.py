import random
import math
from brain_games.main_logic import run_game


TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = list(range(0, random.randint(30,66), random.randint(2,5)))
    answer = str(random.choice(progression))
    string_progression = ' '.join(map(str, progression))
    question = string_progression.replace(answer, '..', 1)
    return(question, answer)


def run_progression_game():
    run_game(get_question_and_answer, TASK)
    return
