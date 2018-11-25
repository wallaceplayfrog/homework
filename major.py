import random

class Major(object):
    def __init__(self, Majorcode, Majorname, Majornum, Majorless):
        self.Majorcode = Majorcode
        self.Majorname = Majorname       
        self.Majornum = Majornum
        self.Majorless = Majorless
        self.mates = []

    def add(self, student):
        self.mates.append(student)
        self.Majorless -= 1
    
    def isFull(self):
        if self.less == 0:
            return True
        else:
            return False

def generateMajor():
    majorString = {1012:('major0'), 
                    2125:('major1'), 
                    4562:('major2'), 
                    1534:('major3'), 
                    1234:('major4'), 
                    2134:('major5'), 
                    4897:('major6'), 
                    1543:('major7'), 
                    4782:('major8'), 
                    1456:('major9'),
                    5487:('major10'),
                    4587:('major12'),
                    6985:('major13'),
                    2145:('major14'),
                    3526:('major15'),
                    8547:('major16')}
    retMajor = []
    i = 0
    for code in majorString:
        i += 1
    j = 0
    while j < i:
        num = random.randint(5,10)#随机生成计划录取人数
        lessnum = num
        retMajor.append(Major(code, majorString[code], num, lessnum))
        j += 1
    return retMajor

print(generateMajor())