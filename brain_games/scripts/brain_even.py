#!/usr/bin/env python
from brain_games.games.even_game import get_question_and_answer
from brain_games.engine import run_game
from brain_games.games.even_game import GAME_DESCRIPTION


def main():
    run_game(get_question_and_answer, GAME_DESCRIPTION)
