import random
secretRandom = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guessestaken in range(1, 7):
    print('take a guess')
    guess = int(input())
    
    if guess > secretRandom:
        print('Your guess is a little too high')
    elif guess < secretRandom:
        print('Your guess is a little too low')
    else:
        break

    if guess == secretRandom:
        print('You have a guessed the right number, it took you ' + str(guessestaken) + 'guesses ' )
    else:
        print('You have not guessed the wrong number, the number I guess was' + str(secretRandom))


        
        





    