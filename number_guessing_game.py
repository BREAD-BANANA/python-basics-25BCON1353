import random


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess_text = input("Your guess (or q to quit): ").strip()

        if guess_text.lower() == "q":
            print(f"The number was {secret_number}. Better luck next time!")
            return

        try:
            guess = int(guess_text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low. Try again!")
        elif guess > secret_number:
            print("Too high. Try again!")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            return


if __name__ == "__main__":
    play_game()
