import random

def display_hangman(incorrect_guesses):
    print("HANGMAN")
    pointer_position = incorrect_guesses
    print(" " * pointer_position + "^")

def get_word():
    words = ["algorithm", "function", "variable", "compile", "iterate",
             "recursion", "binary", "array", "syntax", "pointer"]
    return random.choice(words)

def play_game():
    word = get_word()
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    max_incorrect_guesses = len("HANGMAN") - 1
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    display_hangman(incorrect_guesses)

    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
            if "_" not in guessed_word:
                print("\nCongratulations! You guessed the word:", word)
                print("Phew... you are saved.")
                break
        else:
            print("Wrong guess!")
            incorrect_guesses += 1
            display_hangman(incorrect_guesses)

    if incorrect_guesses == max_incorrect_guesses:
        print("\nYou are hanged. The word was:", word)

def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()

