#!/usr/bin/env python
from brain_games.games import gcd
from brain_games import engine


def main():
    engine.run(gcd.get_question_and_answer, gcd.DESCRIPTION)


if __name__ == '__main__':
    main()
