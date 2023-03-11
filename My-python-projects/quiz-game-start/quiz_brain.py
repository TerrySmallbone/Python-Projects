class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        # print(type(self.question_list[0]))


    def still_has_questions(self):
        return len(self.question_list) > self.question_number


    def next_question(self):
        """Input question list, method will display Q number and ask the questions"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # print(type(current_question))
        answer = input(f"Q{self.question_number}. {current_question['question']}, True or False?")
        self.check_answer(answer, current_question["correct_answer"])


    def check_answer(self, answer, correct_answer):
        # print(answer)
        # print(correct_answer)
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}\n")


