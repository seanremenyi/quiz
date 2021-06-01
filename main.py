from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_bank.append(Question(questions["text"], questions["answer"]))

game = QuizBrain(question_bank)

while game.still_has_questions():
    game.check_answer(game.next_question())

print(f"You completed the Quiz\nYour score is {game.score} out of 12")
