from os import remove, rename

def printInstructions(instructions):
    print(instructions)

def getUserScore(userName):
    try:
        input = open('userscores.txt', 'r')

        for line in input:
            content = line.split(',')
            if content[0] == userName:
                input.close()
                return content[1]
            input.close()
            return '-1'
    except IOError:
        print("File not found, creating a new one :D ...")
        input = open('userscores.txt', 'w')
        input.close()
        return '-1'

def updateUserScore(newUser, userName, score):
    if newUser == True:
        input = open('userscores.txt', 'a')
        input.write(userName + ', ' + score + '\n')
        input.close()
    else:
        temp = open('userScores.tmp', 'w')
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split()
            if content[0] == userName
                
