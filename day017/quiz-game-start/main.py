from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


def create_question():
    question_bank = []
    for question in question_data:
        new_question = Question(question["question"], question["correct_answer"])
        question_bank.append(new_question)
    
    return question_bank

question_bank = create_question()

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")