number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        # New block starts here
        print 'Congratulations, you guessed it.'
        # This causes the while loop to stop
        running = False
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else:
    print 'The while loops is over.'
    # Do anything else you want to do here

print 'Done'
