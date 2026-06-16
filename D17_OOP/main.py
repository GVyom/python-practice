from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for every in question_data:
    question_text = every["text"] #new puesdo variable for text 
    question_answer = every["answer"]
    new_question = Question(question_text,question_answer) #new_question an object or in this instance a list
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You\'ve completed the Quiz')
print(f'Your Final Score was: {quiz.score}/{quiz.question_number}')
