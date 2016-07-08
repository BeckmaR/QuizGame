import tkinter as tk
import PIL.ImageTk, PIL.Image

from quizgame import basequizgen
from .basequizgen import basequizgen
from .question import question

class GuessingGame(tk.Frame):
    def __init__(self, parent, quizgen, *args, **kwargs):
        super().__init__(parent, width=400, height=400, *args, **kwargs)

        if not isinstance(quizgen, basequizgen):
            raise Exception("No proper Quiz Generator given")
        self.quizgen = quizgen

        self.tkimage = None

        self.active_qst = None

        self.answer_frame = tk.Frame(self)

        # configure string vars and labels
        self.questiontext = tk.StringVar()

        self.family_input = tk.StringVar()
        self.plantname_input = tk.StringVar()

        self.var_correct = tk.StringVar()
        self.var_wrong = tk.StringVar()

        self.correct_answer = tk.StringVar()

        self.var_correct.set("Correct: 0")
        self.var_wrong.set("Missed: 0")

        self.correct_answer.set("")

        self.photolabel = tk.Label(self, relief="raised")
        self.questionlabel = tk.Label(self, textvariable=self.questiontext, relief="raised")

        self.family_entry = tk.Entry(self.answer_frame, textvariable=self.family_input)
        self.plantname_entry = tk.Entry(self.answer_frame, textvariable=self.plantname_input)

        self.family_label = tk.Label(self.answer_frame, text="Familie")
        self.plantname_label = tk.Label(self.answer_frame, text="Pflanzenname")

        self.correct_answer_label = tk.Label(self.answer_frame, textvariable=self.correct_answer)

        self.check_button = tk.Button(self.answer_frame, text="Check answer", command=self.check_answer)
        self.next_button = tk.Button(self.answer_frame, text="Next Question", command=self.show_question)

        # show number of wrong / correct attempts
        self.num_correct = 0
        self.num_missed = 0

        self.rateframe = tk.Frame(self)

        self.correct_label = tk.Label(self.rateframe, textvariable=self.var_correct)
        self.wrong_label = tk.Label(self.rateframe, textvariable=self.var_wrong)

        self.default_button_color = self.cget("bg")

        self.set_grid()
        self.show_question()

    def set_grid(self):
        self.photolabel.grid(row=0, padx=10, pady=10)
        self.questionlabel.grid(row=1, pady=(0, 20))

        # inside self.answerframe
        self.family_label.grid(row=0, column=0)
        self.family_entry.grid(row=0, column=1)

        self.plantname_label.grid(row=1, column=0)
        self.plantname_entry.grid(row=1, column=1)

        self.correct_answer_label.grid(row=2, column=0, columnspan=2)

        self.check_button.grid(row=3, column=0)
        self.next_button.grid(row=3, column=1)

        # inside self.rateframe
        self.correct_label.grid(row=0, column=0)
        self.wrong_label.grid(row=0, column=1)

        # grid subframes
        self.rateframe.grid(row=8)

        self.answer_frame.grid(row=2)

        self.grid(row=0, column=0)

    def show_question(self):
        self.active_qst = self.quizgen.get_question()

        print(self.active_qst.correct_answer)

        if self.active_qst is None:
            self.questiontext = "No more questions available"
            return None

        self.check_button.config(state=tk.ACTIVE)
        self.next_button.config(state=tk.DISABLED)

        self.family_entry.config(bg=self.default_button_color)
        self.plantname_entry.config(bg=self.default_button_color)

        self.family_input.set("")
        self.plantname_input.set("")

        self.correct_answer.set("")

        # show image
        maxsize = (600, 400)

        self.active_qst.image.thumbnail(maxsize, PIL.Image.ANTIALIAS)
        img = PIL.ImageTk.PhotoImage(self.active_qst.image)

        self.photolabel.config(image=img)
        self.tkimage = img

        self.photolabel.place(x=0, y=0, width=maxsize[0], height=maxsize[1])
        self.photolabel.grid(row=0)

        self.questiontext.set(self.active_qst.question)

    def check_answer(self):
        self.check_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.ACTIVE)

        correct_answer_parts = self.active_qst.correct_answer.lower().split('-')

        for i, s in enumerate(correct_answer_parts):
            correct_answer_parts[i] = s.strip()

        correct_family = correct_answer_parts[0]
        correct_name = correct_answer_parts[1]

        self.correct_answer.set(correct_family + " - " + correct_name)

        given_family = self.family_input.get().lower().strip()
        given_name = self.plantname_input.get().lower().strip()

        if given_family == correct_family:
            self.num_correct += 1
            self.family_entry.config(bg="green")
        else:
            self.num_missed += 1
            self.family_entry.config(bg="red")

        if given_name == correct_name:
            self.num_correct += 1
            self.plantname_entry.config(bg="green")
        else:
            self.num_missed += 1
            self.plantname_entry.config(bg="red")

        self.update_counter()

    def update_counter(self):
        self.var_correct.set("Correct: " + str(self.num_correct))
        self.var_wrong.set("Wrong: " + str(self.num_missed))








