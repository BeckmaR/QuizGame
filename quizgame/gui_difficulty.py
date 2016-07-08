import tkinter as tk

class difficultyChoser(tk.Frame):
    def __init__(self, parent, possibilities, _callback):
        def callback(s):
            def inner_fun():
                _callback(s)

            return inner_fun

        super().__init__(parent)

        self.grid(row=0, column=0)
        self.grid_rowconfigure(index=0, minsize=100)
        self.grid_columnconfigure(index=0, minsize=400)
        self.diff_buttons = []
        row = 0
        self.explainlabel = tk.Label(self, text="Choose a difficulty!")
        self.explainlabel.grid(row=row)
        for diff in possibilities:
            self.diff_buttons.append(tk.Button(self, text=diff, command=callback(diff)))
            self.diff_buttons[row].grid(row=row + 1)
            row += 1
