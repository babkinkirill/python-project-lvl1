import random
import math


DESCRIPTION = '''Answer "yes" if given number is prime.
Otherwise answer "no".'''


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    number = random.randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return(question, answer)
