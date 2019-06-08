import re
import string
import random

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

# Open the text file with assorted words
open_document = open(file, 'r')
text_file = open_document
# print(text_file)

# Create list of words
word_list = [word.strip() for word in text_file.readlines()]
# print(word_list)

guessed_letters = []

# Choose level of difficulty for Mystery Word Game

def pick_mode(word_list):
    '''Separate word_list into easy, medium, and hard lists based on word length. Return a random word from the appropriate list.'''

    user_input_valid = True
    
    while user_input_valid:
        user_input = input("Welcome to Mystery Word Game. Do you want to play in easy, medium, or hard mode? Select 'E' for Easy, 'M' for Medium, and 'H' for Hard: ")
        if user_input in ("E", "e", "M", "m", "H", "h"):
            if user_input == 'E' or user_input == 'e':
                easy_mode = [word for word in word_list if len(word)>=4 and len(word)<=6]
                hidden_word = random.choice(easy_mode)
                return hidden_word 
            if user_input == 'M' or user_input == 'm':
                medium_mode = [word for word in word_list if len(word)>=6 and len(word)<=8]
                hidden_word = random.choice(medium_mode)
                return hidden_word
            if user_input == 'H' or user_input == 'h':
                hard_mode = [word for word in word_list if len(word)>8]
                hidden_word = random.choice(hard_mode)
                return hidden_word
        else:
            print("Please try again.") 

def guess_word(hidden_word, guessed_letters):
    '''A function to show the letters from the random word that have been guessed correctly. The function also shows '_' for blanks in the random word that have not been guessed or guessed incorrectly.'''

    mystery_word = []
    for letter in hidden_word:
        if letter in guessed_letters:
            mystery_word.append(letter)
        else: 
            mystery_word.append('_')
    
    mystery_word = ' '.join(mystery_word)
    mystery_word = mystery_word.upper()
    return mystery_word

def word_completely_guessed(hidden_word, guessed_letters):
    '''Determines if the random word has been guessed correctly by returning True or False'''

    word_finished = guess_word(hidden_word, guessed_letters)
    if '_' in word_finished:
        return False
    else:
        return True

def play_game(hidden_word):
    '''This function allows the user to guess the letters of the random word.'''
    guessed_letters = []
    guess_counter = 8
    print("Your word is ", len(hidden_word) ," letters.")
    while word_completely_guessed(hidden_word, guessed_letters) == False:
        next_guess = (input("Guess a letter: ")).lower()
        if len(next_guess) > 1:
            print("You can only guess one letter. Please try again: ")
        elif next_guess not in guessed_letters:
            if next_guess not in hidden_word:
                print("Your guess is not in the word.")
                guess_counter -= 1 
            else: 
                print("You guessed a letter in the word!")
        else:
            print("You guessed that letter already. Please try again: ")
        guessed_letters.append(next_guess)
        print(guess_word(hidden_word, guessed_letters))
        print("You have guessed the following letters so far: {}".format(guessed_letters), " and you have {} guesses left.\n".format(guess_counter))
        if guess_counter == 0:
            break
    if guess_counter == 0:
        player_loss = input(("You lost the game. The word was {}. Do you want to play again? (Yes or No)\n".format(hidden_word)))
        player_loss.lower()
            
        if player_loss == 'yes':
            return main()
        else:
            print("Thank you for playing Mystery Word Game!")
    else:
        player_win = input(("You won Mystery Word Game!!! Do you want to play again? (Yes or No)"))
        player_win.lower()
        if player_win == 'yes':
            return main()
        else: 
            print("Thank you for playing Mystery Word Game!")
            
def main():
    '''Play Mystery Word Game'''
    hidden_word = pick_mode(word_list)
    return play_game(hidden_word)

if __name__ == '__main__':
    main()