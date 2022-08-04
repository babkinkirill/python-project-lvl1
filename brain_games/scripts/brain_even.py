#!/usr/bin/env python
from brain_games.games import even
from brain_games.engine import run


def main():
    run(even.get_question_and_answer, even.DESCRIPTION)
