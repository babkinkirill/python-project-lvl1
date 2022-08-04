import prompt


NUMBER_OF_ROUNDS = 3


def run(get_question_and_answer, DESCRIPTION):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(DESCRIPTION)
    for i in range(NUMBER_OF_ROUNDS):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if answer != user_answer:
            print(f''' '{user_answer}' is wrong answer ;(. Correct answer is '{answer}'
Let's try again, {name}!''')
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
