from data import question_data
from question_model import Question
from quiz_brain import quiz_brain
question_bank=[]
for question in question_data["results"]:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
quiz_brain=quiz_brain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.new_question()


