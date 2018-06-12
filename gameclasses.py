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
        elif value > 10:
            self._noOfQuestions = 10
            print("Maximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._noOfQuestions = value

class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input("\nPlease convert %d to binary", %(base10))
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        score + 1
                        print("The answer is correct")
                        break
                    else:
                        print("Wrong answer. The correct answer is {:b}".format(base10))
                        break
                except:
                    print("You did not enter a binary number. Try again.")
                    userResult = input("\nPlease convert %d to binary", %(base10))
    return score

class MathGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '', '']
        operatorDict = {1: "+", 2:"-", 3:"*", 4:"**"}

        for i in range(self.noOfQuestions):
            for j in range(5):
                #j is placeholder index for numberList
                #each instance of j then gets given a random number between 1-9
                numberList[j] = randint(1, 9)
                symbolList[0] = operatorDict[randint(1, 4)]