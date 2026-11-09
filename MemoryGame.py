import os
import random
import time

MIN_VALUE = 1
MAX_VALUE = 101


def generate_sequence(difficulty):
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(difficulty)]


# will move to Utils.py in part 2
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_sequence(sequence):
    print("Memorize this sequence:")
    print(" ".join(str(n) for n in sequence), flush=True)
    time.sleep(0.7)
    clear_screen()


def get_list_from_user(difficulty):
    while True:
        raw = input(f"Enter the {difficulty} number(s) you saw, separated by spaces: ")
        parts = raw.split()
        if len(parts) != difficulty:
            print(f"Please enter exactly {difficulty} number(s).")
            continue
        if not all(p.isascii() and p.isdigit() for p in parts):
            print("Whole numbers only, separated by spaces.")
            continue
        numbers = [int(p) for p in parts]
        if not all(MIN_VALUE <= n <= MAX_VALUE for n in numbers):
            print(f"Each number must be between {MIN_VALUE} and {MAX_VALUE}.")
            continue
        return numbers


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    answer = get_list_from_user(difficulty)
    return is_list_equal(sequence, answer)
