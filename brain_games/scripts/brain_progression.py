#!/usr/bin/env python
from brain_games.games import progression
from brain_games import engine


def main():
    engine.run(progression.get_question_and_answer, progression.DESCRIPTION)
