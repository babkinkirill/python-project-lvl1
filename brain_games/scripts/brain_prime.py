#!/usr/bin/env python
from brain_games.games import prime_game
from brain_games import engine


def main():
    engine.run_game(prime_game.get_question_and_answer,
                    prime_game.GAME_DESCRIPTION)


if __name__ == '__main__':
    main()
