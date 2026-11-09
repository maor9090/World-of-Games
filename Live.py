import GuessGame
import MemoryGame
import CurrencyRouletteGame

GAMES = {1: MemoryGame, 2: GuessGame, 3: CurrencyRouletteGame}


def welcome(name):
    return (f"Hello {name} and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.")


def get_int_in_range(prompt, low, high):
    while True:
        raw = input(prompt).strip()
        # isdigit alone accepts non-ascii digits
        if not (raw.isascii() and raw.isdigit()):
            print(f"Please enter a whole number from {low} to {high}.")
            continue
        value = int(raw)
        if low <= value <= high:
            return value
        print(f"The number must be between {low} and {high}.")


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - remember a sequence of numbers shown for 0.7 seconds")
    print("2. Guess Game - guess the computer's secret number")
    print("3. Currency Roulette - estimate the ILS value of a random USD amount")
    choice = get_int_in_range("Your choice (1-3): ", 1, 3)
    difficulty = get_int_in_range("Please choose game difficulty from 1 to 5: ", 1, 5)

    try:
        result = GAMES[choice].play(difficulty)
    except Exception as e:
        # an error inside a game must never count as a win
        print(f"Round cancelled because of an error: {e}")
        return None

    if result is True:
        print("You won!")
    elif result is False:
        print("You lost.")
    else:
        print("The round did not finish, no result.")
    return result
