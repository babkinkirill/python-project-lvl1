#!/usr/bin/env python
from brain_games.games.calc_game import get_question_and_answer
from brain_games.games.calc_game import GAME_DESCRIPTION
from brain_games.engine import run_game


def main():
    run_game(get_question_and_answer, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
