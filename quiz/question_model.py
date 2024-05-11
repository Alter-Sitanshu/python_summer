from data import *
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0
    
    def next_question(self):
        question = self.q_list[self.q_num]
        self.q_num += 1
        feedback = input(f"Q.{self.q_num} : {question.text} (True/False) : ").title()
        if self.answer_check(feedback=feedback, answer=question.answer):
            self.score +=1
            print(f"Your score is : {self.score}/{self.q_num}\n\n")
        else:
            print(f"Your score is : {self.score}/{self.q_num}\n\n")
            
        
    
    def answer_check(self, feedback, answer):
        if feedback == answer:
            print("You got it right !!")
            return True
        else:
            print("You got it Wrong !!")
            return False
        
    def still_has_questions(self):
        if self.q_num < len(self.q_list):
            return True
        else:
            return False
        


question_bank = []
for index in question_data:
    text = index["text"]
    answer = index["answer"]
    question_bank.append(Question(text=text,answer=answer))

new_quiz = QuizBrain(question_bank)
print(logo)
while new_quiz.still_has_questions():
    new_quiz.next_question()
    