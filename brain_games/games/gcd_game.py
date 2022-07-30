import random
import math
from brain_games.engine import run_game


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = random.randint(1, 50)
    number_two = random.randint(1, 50)
    question = (f'{number_one} {number_two}')
    answer = str(math.gcd(number_one, number_two))
    return(question, answer)


def run_gcd_game():
    run_game(get_question_and_answer, GAME_DESCRIPTION)
    return
