import random
from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

import requests

# free keyless API, asks for attribution: exchangerate-api.com
API_URL = "https://open.er-api.com/v6/latest/USD"
TIMEOUT = 5
CENT = Decimal("0.01")


class RateError(Exception):
    pass


def to_money(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def generate_amount():
    return random.randint(1, 100)


def get_exchange_rate():
    try:
        response = requests.get(API_URL, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError) as e:
        raise RateError(f"could not reach the exchange rate service ({e})") from e

    if not isinstance(data, dict) or data.get("result") != "success":
        raise RateError("the exchange rate service returned an error")
    rates = data.get("rates")
    if not isinstance(rates, dict) or "ILS" not in rates:
        raise RateError("ILS rate missing from the response")

    try:
        rate = Decimal(str(rates["ILS"]))  # str first, avoids float noise
    except InvalidOperation as e:
        raise RateError("ILS rate is not a number") from e
    if not rate.is_finite() or rate <= 0:
        raise RateError("ILS rate is not a positive number")
    return rate


def calculate_ils(amount_usd, rate):
    return to_money(Decimal(amount_usd) * rate)


def get_money_interval(difficulty, total):
    margin = Decimal(5 - difficulty)
    return total - margin, total + margin


def get_guess_from_user(amount_usd):
    while True:
        raw = input(f"How much is {amount_usd} USD worth in ILS? ").strip()
        try:
            guess = Decimal(raw)
            # Decimal also accepts nan and inf
            if not guess.is_finite() or guess < 0:
                raise InvalidOperation
            return to_money(guess)
        except InvalidOperation:
            print("Please enter a non-negative number, e.g. 36 or 35.50.")


def is_within_interval(guess, lower, upper):
    return lower <= guess <= upper


def play(difficulty):
    amount_usd = generate_amount()
    try:
        rate = get_exchange_rate()
    except RateError as e:
        print(f"Round cancelled: {e}.")
        return False

    total = calculate_ils(amount_usd, rate)
    lower, upper = get_money_interval(difficulty, total)
    guess = get_guess_from_user(amount_usd)
    return is_within_interval(guess, lower, upper)
