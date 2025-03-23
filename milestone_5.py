import random

# Create a Hangman class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialise the attributes of the class
        self.word_list = word_list 
        self.num_lives = num_lives  
        self.word = random.choice(self.word_list)  
        self.word_guessed = ['_' for _ in self.word] 
        self.num_letters = len(self.word)  
        self.list_of_guesses = []  

    def check_guess(self, guess):
        # This function checks if the guessed letter is in the word and updates the guessed word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
        else:
            print(f"Oops! {guess} is not in the word.")
            self.num_lives -= 1  

    def display_word(self):
        print("Current word: " + ' '.join(self.word_guessed))

    def is_game_over(self):
        # Check if user either won or lost the game 
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
    num_lives = 5 
    game = Hangman(word_list, num_lives)  

    # Hangman main game loop 
    while not game.is_game_over():
        game.display_word()  # Display the word with underscores
        ask_for_input(game)  # Ask the player for a guess

# List of words for the game 
word_list = ["giraffe", "zebra", "hippopotimous", "bananatree", "jungle"]

play_game(word_list)