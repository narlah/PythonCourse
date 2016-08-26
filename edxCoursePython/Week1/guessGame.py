print "Please think of a number between 0 and 100!"
startPoint, endPoint = 0, 100
guess = 0
inputR = 0
while inputR != 'c':
    guess = (endPoint - startPoint) / 2
    secret = guess + startPoint
    print "guess : " + str(guess) + " guess division " + str(endPoint - startPoint) + " from " + str(
        startPoint) + " to " + str(endPoint)
    print "Is your secret number = " + str(secret)
    inputR = raw_input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly :")
    if inputR not in ['c', 'l', 'h']:
        print "Sorry, I did not understand your input."
    elif inputR == "c":
        print ("Game over. Your secret number was:" + str(secret))
    elif inputR == "h":
        endPoint = secret
    else:
        startPoint += guess