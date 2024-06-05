import requests
import tkinter as tk
import html

parameters = {"amount": 10, "type": "boolean"}
api_fetch = requests.get(url="https://opentdb.com/api.php", params=parameters)
api_fetch.raise_for_status()
question_list = api_fetch.json()["results"]
question_data = [{"question":iter["question"], "answer":iter["correct_answer"]} for iter in question_list]

class QuizBrain:
    question = None
    @classmethod
    def next_question(cls) -> None:
        canvas.config(bg="white")
        true_button.config(state="normal")
        false_button.config(state="normal") 
        global q_num, score
        if cls.still_has_questions():
            cls.question = question_data[q_num]
            q_num += 1
            canvas.itemconfig(question_text, text=html.unescape(cls.question["question"]))
        else:
            true_button.config(state="disabled")
            false_button.config(state="disabled")    
    @classmethod
    def clickHandler(cls, click: str) -> None:
        global score
        feedback = click
        if cls.answer_check(feedback=feedback, answer=cls.question["answer"]):
            score +=1
            score_text.config(text=f"Score : {score}")
            cls.userOutput(True)
        else:
            cls.userOutput(False)

    @classmethod
    def userOutput(cls, answer: bool) -> None:
        true_button.config(state="disabled")
        false_button.config(state="disabled") 
        if answer:
            canvas.config(bg="green")  
        else:
            canvas.config(bg="red")  
        screen.after(1000, cls.next_question) 
    @classmethod
    def answer_check(cls, feedback: str, answer: str) -> bool:
        if feedback == answer:
            return True
        else:
            return False
    @classmethod
    def still_has_questions(cls) -> bool:
        if q_num < len(question_data):
            return True
        else:
            return False
        
#-----Building the GUI-------
q_num = 0
score = 0
screen = tk.Tk()
screen.minsize(width=540, height=400)
screen.config(padx=30, pady=10, bg="#375362")
score_text = tk.Label(master=screen,text=f"Score : {score}", font=("Ariel", 13, "bold"), bg="#375362", fg="white")
score_text.grid(column=0, row=0, padx=5, pady=5)

canvas = tk.Canvas(master=screen, height=350, width=480)
question_text = canvas.create_text(240, 170, text="Hello World", font={"Ariel", 15, "italic"}, fill="#375362", width=460)
canvas.grid(column=0, row=1, columnspan=2, pady=30)

true_button = tk.Button(master=screen, text="True", padx=10, pady=10, fg="white", font={"Ariel", 15, "bold"}, 
                        command= lambda : QuizBrain.clickHandler("True"), bg="#375362", highlightthickness=0)
false_button = tk.Button(master=screen, text="False", padx=10, pady=10, fg = "white", font={"Ariel", 15, "bold"}, 
                         command= lambda : QuizBrain.clickHandler("False"), bg="#375362", highlightthickness=0)
true_button.grid(column=0, row=2, pady=30)
false_button.grid(column=1, row=2, pady=30)

QuizBrain.next_question()
screen.mainloop()
