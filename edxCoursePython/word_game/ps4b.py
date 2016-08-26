from ps4a import *
#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    max = 0
    max_word = ""
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            if score > max:
                max = score
                max_word = word
    return max_word if max > 0 else None

    # return the best word you found.

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    local_hand = hand.copy()
    hand_count = calculateHandlen(local_hand)
    current_score = 0
    while hand_count > 0:
        print "Current Hand: ",
        displayHand(local_hand)
        input_word = compChooseWord(local_hand, wordList, n)
        if input_word == None:
            break
        if not isValidWord(input_word, hand, wordList):
            print "Invalid word, please try again."
            continue
        score_for_input_word = getWordScore(input_word, n)
        current_score += score_for_input_word
        print "\"" + str(input_word) + "\" earned " + str(score_for_input_word) + " points. " + "Total: " + str(
            current_score) + " points"
        local_hand = updateHand(local_hand, input_word)
        hand_count = calculateHandlen(local_hand)
        print
    if hand_count == 0:
        print "Run out of letters.",
    else:
        print "Goodbye!",
    print "Total score: " + str(current_score) + " points."


#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    prev_hand = {}
    while True:
        user_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if user_input == 'e':
            break
        elif (user_input == 'r') & (prev_hand.__len__() == 0):
            print ("You have not played a hand yet. Please play a new hand first!")
            continue
        elif user_input == 'n':
            prev_hand = dealHand(HAND_SIZE)
            choose_player(prev_hand, wordList)
        elif user_input == 'r':
            choose_player(prev_hand, wordList)
        else:
            print("Invalid command.")


def choose_player(prev_hand, wordList):
    while True:
        print
        who_plays = raw_input("Enter u to have yourself play, c to have the computer play:")
        if who_plays == "u":
            playHand(prev_hand, wordList, HAND_SIZE)
            break
        elif who_plays == "c":
            compPlayHand(prev_hand, wordList, HAND_SIZE)
            break
        else:
            print("Invalid command.")


print  #
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
