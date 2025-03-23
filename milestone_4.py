import random 

# Create a Hangman class
class Hangman:
    def __init__(self, word_list, num_lives=5):

        # Initialise the attributes of the class
        self.word_list = word_list  # List of possible words for the game
        self.num_lives = num_lives  # Number of lives the player has (default is 5)

        self.word = random.choice(self.word_list)  # Randomly choose a word from the word list
        self.word_guessed = ['_' for _ in self.word]  # List of underscores for unguessed letters
        self.num_letters = len(self.num_list)  # Number of unique letters in the word
        self.list_of_guesses = []  # List of the guesses that have already been tried

        # Create a "check guess" method 
        def check_guess(self, guess):
            guess = guess.lower()
            if guess in self.word:
                print(f"Good guess!{guess} is in the word.")

        def ask_for_input():
            while True:
                guess = input("Please guess a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a singluar letter. ")
            elif guess in self.list_of_guesses: 
                print("You already tried this letter!")
            
            else: 
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        
        ask_for_input()

# End of Hangman code 





