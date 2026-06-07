from data import game_data
import random

def check_answer(A,B,answer,score):
    if A['follower_count'] > B['follower_count'] and answer == 'lower':
        print("correct!")
        return score + 1, True
    if A['follower_count'] < B['follower_count'] and answer == 'higher':
        print('correct!')
        return score + 1, True
    else:
        print('wrong, sorry you lost!')
        return score, False
    

def play_game():
    while True:
        ready = input('Welcome to Higher Or Lower. Are you ready to play the game? (Y/N): ').lower()
        if ready == 'n':
            print('Sure, Just let us know once you are ready')
        if ready == 'y':
            break
    
    
    score = 0
    A, B = random.sample(game_data, k=2)
    while True:
        print(f'your score is {score}')
        print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}. {A['follower_count']}")
        print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}. {B['follower_count']}")

        answer = input('Please type higher or lower: ').lower()
        score, correct = check_answer(A,B,answer,score)
        if correct:
            A = B
            while True:
                B = random.choice(game_data)
                if B != A:
                    break
        else:
                print(f'final Score: {score}')
                break
    
play_game()
#1. Generate Account A
#2. Generate Account B
#3. Display both accounts
#4. Ask user for choice (A or B)
#5. Compare follower counts
#6. Check if user's choice is correct
#7. If correct:
#      - Increase score
#      - Move B → A
#      - Generate a new B
#      - Repeat
#8. If wrong:
#      - End game
#      - Display final score