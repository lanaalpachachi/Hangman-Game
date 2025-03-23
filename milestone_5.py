import random

# Create a Hangman class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialise the attributes of the class
        self.word_list = word_list  # List of possible words for the game
        self.num_lives = num_lives  # Number of lives the player has (default is 5)
        self.word = random.choice(self.word_list)  # Randomly choose a word from the word list
        self.word_guessed = ['_' for _ in self.word]  # List of underscores for unguessed letters
        self.num_letters = len(self.word)  # Number of letters in the word
        self.list_of_guesses = []  # List of the guesses that have already been tried

    def check_guess(self, guess):
        # This function checks if the guessed letter is in the word and updates the guessed word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        else:
            print(f"Oops! {guess} is not in the word.")
            self.num_lives -= 1  # Decrease the number of lives if the guess is wrong

    def display_word(self):
        # Display the current state of the word with guessed letters
        print("Current word: " + ' '.join(self.word_guessed))

    def is_game_over(self):
        # Check if the game is over (either lost or won)
        if self.num_lives == 0:
            print("You have lost!")
            return True
        elif '_' not in self.word_guessed:
            print("Congratulations! You have guessed the word!")
            return True
        return False

def ask_for_input(game):
    while True:
        guess = input("Please guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif guess in game.list_of_guesses:
            print(f"You already guessed the letter '{guess}'!")
        else:
            game.check_guess(guess)
            game.list_of_guesses.append(guess)
            break

def play_game(word_list):
    num_lives = 5  # Set the number of lives
    game = Hangman(word_list, num_lives)  # Create an instance of the Hangman class

    # Main game loop
    while not game.is_game_over():
        game.display_word()  # Display the word with underscores
        ask_for_input(game)  # Ask the player for a guess

# List of words for the game
word_list = ["python", "hangman", "code", "programming"]

# Start the game
play_game(word_list)