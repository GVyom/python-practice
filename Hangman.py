from hangman_words import hangman_words
from hangman_words import stages
import random

current_word = random.choice(hangman_words)
blanks = len(current_word)

P = ""
for l in range(blanks):
    P += "_"
print(stages[6])
print(P)

gussed_letters = []
game_over = False
lives = 6

while not game_over:
    guess = input("please put a letter here: ").lower()
    if guess in gussed_letters:
        print(stages[lives])
        print('You already gussed the letter')
        continue

    display = ""
    for letter in current_word:
        if letter == guess:
            display += letter
        elif letter in gussed_letters:
            display += letter
        else:
            display += "_"
    print(stages[lives])
    print(display)

    if guess not in gussed_letters: 
        gussed_letters.append(guess)
        
    if display == current_word:
        game_over = True
        print(stages[lives])
        print(f"You win, the word is {current_word}")

    if guess not in current_word:
        lives -= 1
        print(stages[lives])
        print(f'Wrong guess, you have {lives} lives left')
        print(display)

    if lives == 0:
        game_over = True
        print(stages[lives])
        print(f'You are out of lives, correct word is {current_word}')
        