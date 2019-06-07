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

# Choose level of difficulty for Mystery Word Game
user_input = input("Welcome to Mystery Word Game. Do you want to play in easy, medium, or hard mode? Select 'E' for Easy, 'M' for Medium, and 'H' for Hard: ")

def random_word(word_list, user_input):
    '''Separate word_list into easy, medium, and hard lists based on word length. Return a random word from the appropriate list.'''
    
    if user_input == 'E' or user_input == 'e':
        easy_mode = [word for word in word_list if len(word)>=4 and len(word)<=6]
        return print("Your word is ", len(random.choice(easy_mode)) ," letters.")
    
    if user_input == 'M' or user_input == 'm':
        medium_mode = [word for word in word_list if len(word)>=6 and len(word)<=8]
        return print("Your word is ", len(random.choice(medium_mode)) ," letters.")

    if user_input == 'H' or user_input == 'h':
        hard_mode = [word for word in word_list if len(word)>8]
        return print("Your word is ", len(random.choice(hard_mode)) ," letters.")
    
    if user_input != 'E' or user_input != 'e' or user_input != 'M' or user_input != 'm' or user_input != 'H' or user_input != 'h':
        return input("Please select 'E' for easy, 'M' for medium, or 'H' for hard: ") and random_word(word_list, user_input)
    
    

random_word(word_list, user_input)
    