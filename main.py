import random


def guess(x):
    random_num = random.randint(1, x)
    user_guess = 0
    while user_guess != random_num:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))

        if user_guess < random_num:
            print('Sorry your guess is to low.')
        elif user_guess > random_num:
            print('Sorry your guess is to high')
        elif user_guess == random_num:
            print("Good job! You guessed right!")

        else:
            print("Something odd happened. Please run program again.")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' or 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)')
        if feedback == 'h' or "H":
            high = guess - 1
        elif feedback == 'l' or 'L':
            low = guess + 1

    print(f'Yay the computer guessed your number, {guess}, correctly!')


computer_guess(10)
