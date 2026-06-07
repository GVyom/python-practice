from data import game_data
import random

def check_answer(A,B,answer,score): #This check usually is to return True or False value
    if A['follower_count'] > B['follower_count'] and answer == 'lower':
        print("correct!")
        return score + 1, True #used comma as we need to function to add value, plus return Boolean value
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
    while True: #This while is broken from the last "else: break statement"
        print(f'your score is {score}')
        print(f"Compare A: {A['name']}, a {A['description']} from {A['country']}.")
        print(f"Compare B: {B['name']}, a {B['description']} from {B['country']}.")

        answer = input('Please type higher or lower: ').lower()
        score, correct = check_answer(A,B,answer,score) #Output of check_answer function - Score + 1 also check (Boolean)
        if correct: #correct is substituted with value such as True or False as result of check_asnwer output
            A = B
            while True:
                B = random.choice(game_data)
                if B != A: # if we B = A -> it will not run hence while will stay as True
                    break # if B != A then while loop will break
        else: # if correct False (False is only when answer is wrong)
                print(f'final Score: {score}')
                break
    
play_game()
