from data import question_data
from html import unescape
from quiz_brain import QuizBrain
from question_model import Question
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = unescape(question["question"])
    question_answer = unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
