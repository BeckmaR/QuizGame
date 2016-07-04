#!/usr/bin/python3
import tkinter as tk
from quizgame import QuizGame, basequizgen, quizgen_kennkarten

quizgenerator = quizgen_kennkarten("Kennkarten")
root = tk.Tk()
quiz = QuizGame(root, quizgenerator)
root.mainloop()