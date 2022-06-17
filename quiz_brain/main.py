# Quiz

import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for dic in data.question_data:
    question_bank.append(Question(dic["question"], dic["correct_answer"]))

qb = QuizBrain(question_bank)
# repeat while there are still questions remaining
while qb.still_has_questions():
    qb.next_question()
# no need for a + 1 to the question_number here, as it gets increased after the last question is completed

print(f"Your final score is: {qb.score}/{qb.question_number}.")
