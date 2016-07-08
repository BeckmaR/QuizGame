#!/usr/bin/python3
import tkinter as tk
from quizgame import QuizGame, basequizgen, quizgen_kennkarten, basegui

quizgenerator = quizgen_kennkarten("Kennkarten")
root = tk.Tk()
quiz = basegui(root, quizgenerator)
#quiz = QuizGame(root, quizgenerator)
root.mainloop()