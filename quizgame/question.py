import PIL.Image

class question:
    def __init__(self, question, answers, image=None):
        if not isinstance(question, str):
            raise Exception("Question should be a string")
        if not isinstance(answers, list):
            raise Exception("Answers should be a list")
        if len(answers) <= 1:
            raise Exception("More than one answer should be given")
        if image is not None and not isinstance(image, PIL.Image):
            raise Exception("Image is not an instance of PIL.Image")

        self.question = question
        self.answers = answers
        self.image = image
