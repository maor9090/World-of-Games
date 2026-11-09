import random

secret_number = None


def generate_number(difficulty):
    global secret_number
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    while True:
        raw = input(f"Guess the secret number (1 to {difficulty}): ").strip()
        if not (raw.isascii() and raw.isdigit()):
            print(f"Please enter a whole number from 1 to {difficulty}.")
            continue
        guess = int(raw)
        if 1 <= guess <= difficulty:
            return guess
        print(f"The number must be between 1 and {difficulty}.")


def compare_results(guess):
    return guess == secret_number


def play(difficulty):
    generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(guess)
