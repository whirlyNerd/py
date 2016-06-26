import random

def roll():
    print random.randint(1, 6)

raw_input('Press enter to roll the dice:')

roll()

while True:
    choice = raw_input("Press enter to roll again or type quit:")

    if choice != 'quit':
        roll()
    else:
        break
