import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return (question, answer)
