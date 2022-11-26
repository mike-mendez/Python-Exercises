from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_counter = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("JetBrains Mono", 14, "bold"))
        self.score_counter.grid(column=1, row=0)

        self.question_box = Canvas(width=300, height=250, relief="raised")
        self.question_txt = self.question_box.create_text(150, 125, text="", fill=THEME_COLOR,
                                                          font=("JetBrains Mono", 14, "italic"), width=280)
        self.question_box.grid(column=0, columnspan=2, row=1, pady=50)

        true_btn_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_btn_img, bg=THEME_COLOR, highlightthickness=0, relief="flat",
                               command=lambda answer="True": self.btn_press(answer))
        self.true_btn.grid(column=0, row=2)

        false_btn_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_btn_img, bg=THEME_COLOR, highlightthickness=0, relief="flat",
                                command=lambda answer="False": self.btn_press(answer))
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg="white")
        self.score_counter.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_txt = self.quiz.next_question()
            self.question_box.itemconfig(self.question_txt, text=q_txt)
        else:
            self.question_box.itemconfig(self.question_txt,
                                         text=f"You've completed the quiz.\nYour final score was: {self.quiz.score}/"
                                              f"{self.quiz.question_number}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def btn_press(self, answer: str):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")

        self.window.after(1000, self.get_next_question)
