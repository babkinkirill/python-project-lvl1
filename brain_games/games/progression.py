import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = list(range(0, random.randint(30, 66), random.randint(2, 5)))
    answer = str(random.choice(progression))
    modified_progression = ' '.join(map(str, progression))
    question = modified_progression.replace(answer, '..', 1)
    return(question, answer)
