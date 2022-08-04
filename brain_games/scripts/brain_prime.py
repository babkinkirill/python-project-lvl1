#!/usr/bin/env python
from brain_games.games import prime
from brain_games import engine


def main():
    engine.run(prime.get_question_and_answer, prime.DESCRIPTION)
