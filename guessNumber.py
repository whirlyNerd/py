import random

number = random.randint(1, 100)

while True:
    guess = int(raw_input("Guess the number between 1 and 100:"))

    if guess == number:
        print 'Good guess! Please play again.'
        break
    elif guess > number:
        print 'Too high'
        continue
    elif guess < number:
        print 'Too low'
        continue
print 'Thanks for playing!'
