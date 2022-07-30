#!/usr/bin/env python
from brain_games.games.gcd_game import get_question_and_answer
from brain_games.games.gcd_game import GAME_DESCRIPTION
from brain_games import engine


def main():
    engine.run_game(get_question_and_answer, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
