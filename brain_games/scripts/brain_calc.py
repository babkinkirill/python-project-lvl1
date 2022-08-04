#!/usr/bin/env python
from brain_games import engine
from brain_games.games import calc


def main():
    engine.run(calc.get_question_and_answer, calc.DESCRIPTION)


if __name__ == '__main__':
    main()
