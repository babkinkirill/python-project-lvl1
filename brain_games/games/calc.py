import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    math_symbols = ['+', '-', '*']
    math_symbol = random.choice(math_symbols)
    question = (f'{number_one} {math_symbol} {number_two}')
    if math_symbol == '+':
        answer = str(operator.add(number_one, number_two))
    elif math_symbol == '-':
        answer = str(operator.sub(number_one, number_two))
    elif math_symbol == '*':
        answer = str(operator.mul(number_one, number_two))
    return (question, answer)
