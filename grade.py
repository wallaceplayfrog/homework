import random

class StuIfo(object):
    def __init__(self, name, age, snum, sex):
        self.name = name
        self.age = age
        self.snum = snum
        self.sex = sex
        self.scores = {}
        self.will = [1049]

    def setWill(self, wills):
        self.will.extend(wills)

    def setScores(self, subject, score):
        self.scores[subject] = score
    
    def getName(self):
        return self.name

    def getScore(self, subject):
        return self.scores.get(subject, -1)
    
    def setFullscore(self, fullscore):
        self.scores = fullscore
    
    def personPrint(self):
        print(self.name, self.snum, self.age, self.sex)
        print(self.scores)
        print(self.will)  

def generateWill():
    willstring = [1012, 2125, 4562, 1534, 1234, 1234, 4897, 1543, 4782, 1456]
    willLen = 5
    wills = []
    idx = 0
    while idx < willLen:
        willidx = random.randint(0,9)
        temp = willstring[willidx]
        wills.append(temp)
        idx = idx + 1
    return wills

#随机生成姓名
def generateName():
    nameString = "abcdefghijklmnopqrstuvwxyz"
    nameLen = random.randint(2,3)

    retName = ""

    idx = 0
    while idx < nameLen:
        strIdx = random.randint(0,25)
        retName = retName + nameString[strIdx]
        idx = idx + 1
        
    return retName

#随机生成学号
def generateSnum():   
    return random.randint(1000,9999)

#构造年龄
def generateAge():
    return random.randint(18,20)
    
#构造性别
def generateSex():
    constSex = ["male","female"]
    prob = random.uniform(0,1)
    if prob >= 0.5:
        return "male"
    else:
        return "female"

#随机生成4个成绩
def generate4Score():
    chineseScore = random.randint(80,150)
    mathScore = random.randint(80,150)
    englishScore = random.randint(80,150)
    compScore = random.randint(150,300)

    return {"total": chineseScore + mathScore + englishScore + compScore, "chinese": chineseScore, "math": mathScore, "english": englishScore, "comprehensive": compScore}

#随机生成信息
class RandIfo(object):
    def __init__(self, idx):
        self.mates = []
        self.id = idx
        idx = 0
        while idx < 100:
            name = generateName()
            age = generateAge()
            sex = generateSex()
            snum = generateSnum()
            scores = generate4Score()
            will = generateWill()

            tmpStuIfo = StuIfo(name, age, snum, sex)
            tmpStuIfo.setFullscore(scores)
            tmpStuIfo.setWill(will)

            self.mates.append(tmpStuIfo)

            idx = idx + 1

    def myPrint(self):
        print(self.id)
        for person in self.mates:
            person.personPrint()

#myClass = RandIfo("2333333333")
#myClass.myPrint()
