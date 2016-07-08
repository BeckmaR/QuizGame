import PIL.Image


class question:
    def __init__(self, question, answers, correct_answer, image=None):
        if not isinstance(question, str):
            raise Exception("Question should be a string")
        if not isinstance(answers, list):
            raise Exception("Answers should be a list")
        if not isinstance(correct_answer, str):
            raise Exception("Correct answer is not a string!")
        if correct_answer not in answers:
            raise Exception("Correct answer is not in given answers!")
        if image is not None and not isinstance(image, PIL.Image.Image):
            raise Exception("Image is not an instance of PIL.Image")

        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.image = image
