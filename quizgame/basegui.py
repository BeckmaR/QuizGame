import tkinter as tk

from .basequizgen import basequizgen
from .quizgame import QuizGame
from .gui_difficulty import difficultyChoser
from .guessinggame import GuessingGame


class basegui(tk.Frame):
    def __init__(self, parent, quizgen, *args, **kwargs):
        super().__init__(parent, width=400, height=400, *args, **kwargs)
        self.parent = parent

        self.grid(row=0, column=0)

        if not isinstance(quizgen, basequizgen):
            raise Exception("No proper Quiz Generator given")
        self.quizgen = quizgen

        self.difficulties = self.quizgen.get_difficulties()

        self.difficulty_chooser = difficultyChoser(self, self.difficulties, self.set_possibility)

        self.quizgame = None

    def set_possibility(self, s):
        self.difficulty_chooser.grid_forget()
        self.quizgen.set_difficulty(s)

        if s != "pro":
            self.quizgame = QuizGame(self, self.quizgen)

        if s == "pro":
            self.quizgame = GuessingGame(self, self.quizgen)
