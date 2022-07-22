import prompt


def run_game(get_question_and_answer, TASK):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(TASK)
    i = 1
    while i <= 3:
        question, answer, user_answer = get_question_and_answer()
        print(f'Question: {question}')
        if answer == user_answer:
            print('Correct!')
        else:
            print(f''' '{user_answer}' is wrong answer ;(. Correct answer is '{answer}'
Let's try again, {name}!''')
            return
        i += 1
    print(f'Congratulations, {name}!')
    return
