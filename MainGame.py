from Live import welcome, load_game


def main():
    name = ""
    while not name:
        name = input("What is your name? ").strip()
        if not name:
            print("Name cannot be empty.")
    print(welcome(name))
    load_game()


if __name__ == "__main__":
    main()
