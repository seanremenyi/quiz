class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        ask = self.question_list[self.question_number].text
        self.question_number += 1
        guess = input(f"Q.{self.question_number}. {ask} (True/False)? ")
        return guess

    def check_answer(self, guess):
        if guess == self.question_list[self.question_number - 1].answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The Answer was {self.question_list[self.question_number - 1].answer}\nYour score is {self.score}/"
              f"{self.question_number}\n")
