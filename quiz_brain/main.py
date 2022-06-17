# Quiz

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

qb = QuizBrain(question_bank)
# repeat while there are still questions remaining

limit = int(input("How many questions do you wish for? : "))

while qb.still_has_questions(limit):
    qb.next_question()d

print(f"You've completed the quiz with a final score of {qb.score} out of {qb.question_number}.")
