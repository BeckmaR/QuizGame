import tkinter as tk
import PIL.ImageTk, PIL.Image

from quizgame import basequizgen
from .basequizgen import basequizgen
from .question import question

class QuizGame(tk.Frame):
    def __init__(self, parent, quizgen, *args, **kwargs):
        super(QuizGame, self).__init__(parent, width=400, height=400, *args, **kwargs)
        self.parent = parent

        if not isinstance(quizgen, basequizgen):
            raise Exception("No proper Quiz Generator given")
        self.quizgen = quizgen

        self.tkimage = None

        self.num_answers = 4

        # configure string vars and labels
        self.questiontext = tk.StringVar()

        self.photolabel = tk.Label(self.parent, relief="raised")
        self.questionlabel = tk.Label(self.parent, textvariable=self.questiontext, relief="raised")

        # configure answer buttons
        self.answers = []
        self.answerbuttons = []
        self.callbacks = [
            self.button1,
            self.button2,
            self.button3,
            self.button4
        ]

        for i in range(0, 4):
            self.answers.append(tk.StringVar())
            self.answerbuttons.append(
                tk.Button(self.parent, textvariable=self.answers[i], state=tk.DISABLED, command=self.callbacks[i])
            )

        self.next_button = tk.Button(self.parent, text="Next Question", command=self.show_question)

        # show number of wrong / correct attempts
        self.num_correct = 0
        self.num_wrong = 0

        self.var_correct = tk.StringVar()
        self.var_wrong = tk.StringVar()

        self.var_correct.set("Correct: 0")
        self.var_wrong.set("Wrong: 0")

        self.rateframe = tk.Frame(self.parent)

        self.correct_label = tk.Label(self.rateframe, textvariable=self.var_correct)
        self.wrong_label = tk.Label(self.rateframe, textvariable=self.var_wrong)

        self.default_button_color = self.parent.cget("bg")

        self.set_grid()
        self.show_question()

    def set_grid(self):
        self.photolabel.grid(row=0, padx=10, pady=10)
        self.questionlabel.grid(row=1, pady=(0, 20))

        for i in range(0, 4):
            self.answerbuttons[i].grid(row=2+i)

        self.next_button.grid(row=7, pady=(10, 0))

        self.rateframe.grid(row=8, pady=(10, 10))

        #inside self.rateframe
        self.correct_label.grid(row=0, column=0)
        self.wrong_label.grid(row=0, column=1)


    def show_question(self):
        self.active_qst = self.quizgen.get_question()

        if self.active_qst is None:
            self.questiontext = "No more questions available"
            return

        self.next_button.config(state=tk.DISABLED)
        for but in self.answerbuttons:
            but.config(state=tk.ACTIVE)
        for but in self.answerbuttons:
            but.config(background=self.default_button_color, activebackground=self.default_button_color)

        self.active_qst = self.quizgen.get_question()

        # show image
        maxsize = (600, 400)

        self.active_qst.image.thumbnail(maxsize, PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(self.active_qst.image)

        self.photolabel.config(image=img)
        self.tkimage = img

        self.photolabel.place(x=0,y=0, width=maxsize[0], height=maxsize[1])
        self.photolabel.grid(row=0)

        self.questiontext.set(self.active_qst.question)

        for i, buttontext in enumerate(self.answers):
            buttontext.set(self.active_qst.answers[i])

    def update_counter(self):
        self.var_correct.set("Correct: " + str(self.num_correct))
        self.var_wrong.set("Wrong: " + str(self.num_wrong))

    def button1(self):
        self.mark_if_button_wrong(0)
        self.mark_correct_button()

    def button2(self):
        self.mark_if_button_wrong(1)
        self.mark_correct_button()

    def button3(self):
        self.mark_if_button_wrong(2)
        self.mark_correct_button()

    def button4(self):
        self.mark_if_button_wrong(3)
        self.mark_correct_button()

    def mark_if_button_wrong(self, i):
        if self.answers[i].get() != self.active_qst.correct_answer:
            self.answerbuttons[i].config(background="red", activebackground="red")
            self.num_wrong += 1
        else:
            self.num_correct += 1
        self.mark_correct_button()
        self.update_counter()

    def mark_correct_button(self):
        self.next_button.config(state=tk.ACTIVE)
        for but in self.answerbuttons:
            but.config(state=tk.DISABLED)
        for i, but in enumerate(self.answerbuttons):
            if self.answers[i].get() == self.active_qst.correct_answer:
                but.config(background="green", activebackground="green")






