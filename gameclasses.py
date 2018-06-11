class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("Minimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
        else if value > 10:
            self._noOfQuestions = 10
            print("Maximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._noOfQuestions = value

class BinaryGame:
    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
