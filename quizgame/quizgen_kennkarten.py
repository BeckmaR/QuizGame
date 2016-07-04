from .question import question
from .basequizgen import basequizgen
import os, random, PIL.Image

class quizgen_kennkarten(basequizgen):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.files = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            self.files.extend(filenames)

        # shuffle file list!
        random.shuffle(self.files)

        self.index = 0

        self.possible_difficulties = ["normal", "high", "expert"]

        # generate family groupings for higher difficulty questions
        self.families = {}

        for f in self.files:
            family = f.split('-')[0].strip()

            if family not in self.families.keys():
                self.families[family] = []
            self.families[family].append(os.path.splitext(f)[0])


    def get_question(self):
        try:
            file = self.files[self.index]
        except IndexError:
            return None

        self.index += 1

        answers = self.generate_answers(file)

        correct_answer = self.get_plant_name(file)

        img = PIL.Image.open(os.path.join(self.path, file))
        question_text = "Wie heißt diese Pflanze?"

        return question(question_text, answers, correct_answer, img)

    def generate_answers(self, correct_answer):
        chosen_difficulty = self.difficulty

        if chosen_difficulty == "expert":
            correct_family = self.get_family_name(correct_answer)
            if len(self.families[correct_family]) > 4:
                correct_answer = self.get_plant_name(correct_answer)
                while True:
                    more_answers = random.sample(self.families[correct_family], 3)
                    if correct_answer not in more_answers:
                        answers = more_answers
                        answers.append(correct_answer)
                        break
            elif len(self.families[correct_family]) == 4:
                answers = self.families[correct_family]
            else:
                chosen_difficulty = "high"  # fallback to simpler selection


        if chosen_difficulty == "high":
            correct_family = self.get_family_name(correct_answer)
            # choose another one from same family, if available, else fallback to normal mode
            if len(self.families[correct_family]) > 1:
                while True:
                    other_answer = random.choice(self.families[correct_family])
                    if other_answer != self.get_plant_name(correct_answer):
                        answers = [
                            self.get_plant_name(correct_answer),
                            other_answer
                        ]
                        break
                while True:
                    other_family = random.choice(list(self.families.keys()))
                    if other_family != correct_family and len(self.families[other_family]) > 1:
                        break
                answers.extend(random.sample(self.families[other_family], 2))
            else: # if not more than one plant available from family, shuffle completely
                chosen_difficulty = "normal"  # fallback

        if chosen_difficulty == "normal":
            while True:
                answers = random.sample(self.files, 3)
                if correct_answer not in answers:
                    break

            answers.append(correct_answer)

            for i, ans in enumerate(answers):
                answers[i] = self.get_plant_name(ans)

        #random.shuffle(answers)
        return answers

    def get_plant_name(self, filename):
        return os.path.splitext(filename)[0]

    def get_family_name(self, name):
        return name.split('-')[0].strip()





