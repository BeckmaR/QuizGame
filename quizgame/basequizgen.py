from .question import question
import PIL.Image

class basequizgen:
    def __init__(self, *args, **kwargs):
        self.difficulty = None

        self.possible_difficulties = ["normal"]

    def get_question(self):
        qst = "This is a testquestion, answer 1 is correct"
        answers = ["Answer 1", "Answer 2", "Answer 3", "Answer 4"]
        img = PIL.Image.open("quizgame/example_image.jpg")
        return question(qst, answers, "Answer 1", img)

    def get_difficulties(self):
        return self.possible_difficulties

    def set_difficulty(self, diff):
        if diff in self.possible_difficulties:
            self.difficulty = diff
        else:
            raise Exception("Difficulty Level not allowed")


