import random

class SchIfo(object):
    def __init__(self, schCode, schName):
        self.schCode = schCode
        self.schName = schName
        self.major = {}
    
    def addMajor(self, Mcode, Mname, Mnum):
        self.major[Mcode] = [Mname,Mnum]
    
    def setFullMajor(self, fullmajor):
        self.major = fullmajor

    def myPrint(self):
        print(self.schCode, self.schName)
        for key in self.major:
            print(key, self.major[key], "\n")
    
def generateMajor():
    nameString = ["jk", "xa", "wla", "jx", "zdh", "sa", "sad", "bbq", "ncf", "cde"]
    codestring = [1012, 2125, 4562, 1534, 1234, 1234, 4897, 1543, 4782, 1456]

    idx = 0
    retMajor = {}

    while idx < len(nameString):
        tmpname = nameString[idx]
        tmpcode = codestring[idx]
        tmpnum = random.randint(10,20)
        retMajor[tmpcode] = [tmpname, tmpnum]
        idx = idx + 1
    
    return retMajor

#bjut = SchIfo(1049, "bjut")
#bjut.major = generateMajor()
#bjut.myPrint()