import prompt


def run_game(get_question_and_answer, GAME_DESCRIPTION):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(GAME_DESCRIPTION)
    number_of_rounds = 3
    for i in range(number_of_rounds):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if answer == user_answer:
            print('Correct!')
        else:
            print(f''' '{user_answer}' is wrong answer ;(. Correct answer is '{answer}'
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
    return
