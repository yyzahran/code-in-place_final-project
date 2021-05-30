"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


# LEXICON_FILE = "cid_final\Lexicon.txt"    # File to read word list from
LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Takes a word as an argument, and asks the user for guesses (letter) that they think is in the
    word, then it processes the letter added. It allows a fixed amount of wrong guesses and if the user exceeds those, 
    they lose and the word is displayed. If the user win, they get a message saysing so.
    The entry should be one letter, if it is more than one letter, it tells the user than the entry is not
    correct and does not count this a failed try. If the entry is not alphabetical, the guess is counted as a wrong guess and
    the user is asked to provide a valid letter again.
    """
    # dashes represents the selected word (secret_word) as dashes so if the word has 5 letters, dashes will be '-----'
    dashes = len(secret_word) * '-'
    guess_count = 0 # to track how many wrong guesses the user made
    print("The word now looks like this: {}".format(dashes))
    print("You have {} guesses left".format(INITIAL_GUESSES))
    # while loop to track the guesses made by the user, if the worng guesses == the initial_guesses, the loop is exited and the user loses
    while guess_count < INITIAL_GUESSES:
        letter = input("Type a single letter here, then press enter: ") # asking the user for input (i.e. a letter)
        if len(letter) == 1 and letter.isalpha(): # checks if the entry is valid
            if letter.upper() in secret_word: # if the entered letter is in the word
                idx = [] 
                # this for block gets the indices of the entered letter in the secret_word, so we can have its position in the word and
                # adds it to a string
                for i in range(len(secret_word)):
                    if secret_word[i] == letter.upper():
                        idx.append(i)
                # this block tadds he letter to its approporaite place in the dashes string
                for i in idx:
                    dashes = [x for x in dashes] # transforms the dashes string to a list if '-' and length len(dashes)
                    dashes[i] = letter.upper() # replaces the dash at the index i with the letter 
                dashes = ''.join(dashes) # returns dashes back to a string
            
                print("That guess is correct") 
                # a check is all lettters have been added, it will display the word and break out
                # of the while loop, ending the game
                if secret_word == dashes: # winning scenario
                    print("Congrats! The word is: {}".format(secret_word))
                    break
                print('The word now looks like this: {}'.format(dashes)) # lets the user know how the word looks like now
                print("You have {} guesses left".format(INITIAL_GUESSES-guess_count)) # tells the user how many guesses left
            # if the letter is not in the secret_word, it lets the user know how many guesses left
            else:
                guess_count += 1
                print("There are no {}s in the word".format(letter.upper()))
                print('The word now looks like this: {}'.format(dashes))
                print("You have {} guesses left".format(INITIAL_GUESSES-guess_count))
        # a check if the entry is not valid (i.e. aa or an empty string) - a string of more than one character (does not count as a wrong guess)
        elif (len(letter) > 1 and letter.isalpha()) or letter == '':
            print("Guess should only be a single character.")
        # if the entry is not alphabetical (i.e. numbers or symbols), it lets the user know the guess is invalid (counts as a wrong guess)
        else:
            guess_count += 1
            print("Guess should only be a single character.")
            print("You have {} guesses left".format(INITIAL_GUESSES-guess_count))

    # losing scenario
    if guess_count == INITIAL_GUESSES:
        print("Sorry, you lost. The secret word was: {}".format(secret_word))


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.
    """
    words = []
    # reads every line in the file, remove the newline character and adds the line(word) to a list
    with open(LEXICON_FILE) as f:
        for line in f:
            line = line.strip()
            words.append(line)
    # chooses a random word from the list words
    rando = random.choice(words)
    print("For debugging/demo purposes, I am printing the word: {}".format(rando)) # for debugging purposes
    return rando


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()