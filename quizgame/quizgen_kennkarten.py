from .question import question
from .basequizgen import basequizgen
import os, random, PIL.Image

class quizgen_kennkarten(basequizgen):
    def __init__(self, path):
        self.path = path
        self.files = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            self.files.extend(filenames)

        # shuffle file list!
        random.shuffle(self.files)

        self.index = 0

    def get_question(self):
        try:
            file = self.files[self.index]
        except IndexError:
            return None

        self.index += 1

        # make sure answer is not doubled
        while True:
            answers = random.sample(self.files, 3)
            if file not in answers:
                break

        answers.append(file)

        for i, ans in enumerate(answers):
            plant_name, ext = os.path.splitext(ans)
            answers[i] = plant_name

        random.shuffle(answers)

        correct_answer, ext = os.path.splitext(file)

        img = PIL.Image.open(os.path.join(self.path, file))
        question_text = "Wie heißt diese Pflanze?"

        return question(question_text, answers, correct_answer, img)




