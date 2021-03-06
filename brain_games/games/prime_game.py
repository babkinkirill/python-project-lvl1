import random
import math


GAME_DESCRIPTION = '''Answer "yes" if given number is prime.
Otherwise answer "no".'''


def is_prime(question):
    k = 0
    for i in range(2, int(math.sqrt(question) + 1)):
        if question % i == 0:
            k = k + 1
            return False
    return True


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return(question, answer)
