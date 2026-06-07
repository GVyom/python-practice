import random

def set_difficulty():
    Difficulty = input('Please Select Your How Difficult you want game to be?: (easy/hard)').lower()
    while True:
        if Difficulty == 'easy':
            return 10
        elif Difficulty == 'hard':
            return 5
        
        print('Please type valid response')   
    
def check_answer(guess, attempt, answer):
    if guess > answer:
        print('Too High')
        return attempt - 1
    elif guess < answer:
        print('Too Low')
        return attempt - 1
    else:
        print(f'You Got it! Correct guess is {guess}')
        return None

def play_game():
    print('Welcome to the Guessing Game!\nI am thinking of a number between 1 and 100, can you guess it?')
    answer = random.randint(1,100)
    attempt = set_difficulty()

    while attempt > 0:
        print(f'You have {attempt} attempts remaining.')
        guess = int(input('Make a guess: '))

        attempt = check_answer(guess, attempt, answer)

        if guess == answer:
            break
    
    if attempt == 0:
        print(f'You\'ve run out of guesses. The number was {answer}')

play_game()