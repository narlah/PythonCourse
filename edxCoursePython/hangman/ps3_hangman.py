import random
import string


# 6.00 Problem Set 3
# 
# Hangman game
#



def hangman(secretWord=""):
    '''
    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    Nguesses = 8
    list_guesses = []
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    while Nguesses > 0 and (not isWordGuessed(secretWord, list_guesses)) :
        print "-------------"
        print "You have " + str(Nguesses) + " guesses left."
        print "Available letters: " + getAvailableLetters("".join(list_guesses))
        guess = raw_input("Please guess a letter: ").lower()
        if list_guesses.__contains__(guess):
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, list_guesses)
        elif secretWord.__contains__(guess):
            list_guesses.append(guess)
            print "Good guess: " + getGuessedWord(secretWord, list_guesses)
        else:
            list_guesses.append(guess)
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, list_guesses)
            Nguesses -= 1
    print "-------------"
    if isWordGuessed(secretWord, list_guesses):
        print "Congratulations, you won!"
    else:
        print "Sorry, you ran out of guesses. The word was" + secretWord + "."


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    set_without_duplicates = set(secretWord)
    for x in lettersGuessed:
        if set_without_duplicates.__contains__(x):
            set_without_duplicates.remove(x)
    if len(set_without_duplicates) != 0:
        return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    newWord = secretWord
    for x in secretWord:
        if not lettersGuessed.__contains__(x):
            newWord = newWord.replace(x, '_ ')
    return newWord


def getAvailableLetters(lettersGuessed):
    difference = set.difference(set(string.ascii_lowercase), lettersGuessed)
    return "".join(sorted(difference))


# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)



WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
words = loadWords()
# hangman(chooseWord(loadWords()))
hangman("wasguanabana")
