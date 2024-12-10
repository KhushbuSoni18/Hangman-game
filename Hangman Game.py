import random

# List of words for the game
words = ["python", "github", "hangman", "project", "developer"]

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Hangman game function
def hangman():
    print("Welcome to Hangman!")
    word = random.choice(words)  # Randomly select a word
    guessed_letters = set()     # Store guessed letters
    attempts = 6                # Number of incorrect attempts allowed

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Wrong guess!")

        # Check if all letters in the word have been guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
