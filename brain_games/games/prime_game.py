import random
from brain_games.main_logic import run_game


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    k = 0
    for i in range(2, (question // 2) + 1):
            if (question % i == 0):
                 k += 1
    if k <= 0:
        return True
    else:
        return False


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no' 
    return(question, answer)


def run_prime_game():
    run_game(get_question_and_answer, TASK)
    return