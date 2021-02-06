import random


languages = ['python', 'java', 'kotlin', 'javascript']
language = random.choice(languages)
print('H A N G M A N')
option = input('Type "play" to play the game, "exit" to quit: ')
if option == 'exit':
    exit()
print()
guess = '-' * len(language)
counter = 8
print(guess)
letters = set()
while counter > 0:
    letter = input('Input a letter: ')
    if len(letter) != 1:
        print('You should input a single letter')
        print()
        print(guess)
    elif not letter.isalpha() or not letter.islower():
        print('Please enter a lowercase English letter')
        print()
        print(guess)
    elif letter in language and letter not in letters:
        indices = []
        llanguage = list(language)
        idx = 0
        for i in range(llanguage.count(letter)):
            idx = llanguage.index(letter, idx)
            indices.append(idx)
            idx += 1
        lguess = list(guess)
        for i in indices:
            lguess[i] = letter
        guess = ''.join(lguess)
        print()
        print(guess)
        letters.add(letter)
        if guess == language:
            print(f'You guessed the word {guess}!')
            print('You survived!')
            break
    elif letter in letters:
        print("You've already guessed this letter")
        print()
        print(guess)
    else:
        counter -= 1
        letters.add(letter)
        print("That letter doesn't appear in the word")
        if counter <= 0:
            print('You lost!')
            break
        else:
            print()
            print(guess)
