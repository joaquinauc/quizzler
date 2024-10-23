from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="test", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Buttons
        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, command=self.answer_true)
        self.false_btn.grid(column=1, row=2)

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_btn_img, highlightthickness=0, command=self.answer_false)
        self.true_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer_true(self):
        self.feedback("true")

    def answer_false(self):
        self.feedback("false")

    def feedback(self, answer):
        if self.quiz.check_answer(answer):
            feedback_color = "#AEFF90"
        else:
            feedback_color = "#FF9090"
        self.canvas.config(bg=feedback_color)
        self.window.after(1000, self.get_next_question)
