x = 20
number = input('Type your number, then press enter: ')
if float(number) > x:
    print ('Your number is greater than mine.')
elif float(number) < x:
    print ('Your number is less than mine.')
else:
    print('Your number equals my number!')

# Constants go in screaming snake case.

# Raw user input
guess = input('Type a number and press Enter: ')

# Basic sanitization: remove leading and trailing whitespace
# (ALWAYS ALWAYS ALWAYS sanitize user input!)
guess_clean = guess.strip()

# Cast guess to float because user might guess a number with decimals.
# Casting to int would throw an error in that case.
guess_num = float(guess_clean)

# Even though our hidden number is an int, we can compare it to the
# guess because Python automatically converts ints to floats before
# comparing them.
if guess_num < HIDDEN_NUMBER:
    print('Too low!')
elif guess_num > HIDDEN_NUMBER:
    print('Too high!')
else:
    # If the guess is
    #
    #   A) Not less than our hidden number
    #   B) Not greater than our number
    #
    # then the two *must* be equal.
    print('Correct!')
