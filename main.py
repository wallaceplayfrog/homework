import random
from tkinter import *
from copy import deepcopy
import tkinter.messagebox as messagebox

#==========================school class=============================== 
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

class SchIfo(object):
    def __init__(self, schCode, schName):
        self.schCode = schCode
        self.schName = schName
        self.major = generateMajor()
    
    def addMajor(self, Mcode, Mname, Mnum):
        self.major[Mcode] = [Mname,Mnum]
    
    def setFullMajor(self, fullmajor):
        self.major = fullmajor

    def myPrint(self):
        print(self.schCode, self.schName, '\n')
        for key in self.major:
            print(key, self.major[key])
   
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

    for code in majorString:
        num = random.randint(5,10)#随机生成计划录取人数
        lessnum = num
        retMajor.append(Major(code, majorString[code], num, lessnum))

    return retMajor

#====================================student class====================
class StuIfo(object):
    def __init__(self, name, age, snum, sex):
        self.name = name
        self.age = age
        self.snum = snum
        self.sex = sex
        self.scores = {}
        self.will = []
        self.schoolwill = 1049
        self.isAdmit = False

    #操作符重载... :)
    def __lt__(self, other):#operator <     
        return self.scores['total'] < other.scores['total'] 

    def __ge__(self,other):#oprator >= 
        return self.scores['total'] >= other.scores['total'] 
    
    def __le__(self,other):#oprator <= 
        return self.scores['total'] <= other.scores['total']   

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
    
    def strIfo(self):
        tmpinf = []
        tmpinf.append(str(self.snum))
        tmpinf.append(self.name)
        tmpinf.append(str('%s' %self.age))
        tmpinf.append(self.sex)
        for key in self.scores:
            tmpinf.append('%s' %(self.scores[key]))
        tmpinf.append('  '.join('%s' %id for id in self.will))
        return tmpinf

def generateWill():
    willstring = [1012, 2125, 4562, 1534, 1234, 2134, 4897, 1543, 4782, 1456, 5487, 4587, 6985, 2145, 3526, 8547]
    willLen = 5
    will = []
    idx = 0
    while idx < willLen:
        willidx = random.randint(0, len(willstring)-1)
        temp = willstring[willidx]
        willstring.pop(willidx)
        will.append(temp)        
        idx = idx + 1
    return will

#随机生成姓名
def generateName():
    nameString = 'abcdefghijklmnopqrstuvwxyz'
    nameLen = random.randint(2,6)

    retName = ''

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
    constSex = ['male','female']
    prob = random.uniform(0,1)
    if prob >= 0.5:
        return 'male'
    else:
        return 'female'

#随机生成4个成绩
def generate4Score():
    chineseScore = random.randint(80,150)
    mathScore = random.randint(80,150)
    englishScore = random.randint(80,150)
    compScore = random.randint(150,300)

    return {'total': chineseScore + mathScore + englishScore + compScore, 
            'chinese': chineseScore, 
            'math': mathScore, 
            'english': englishScore, 
            'comprehensive': compScore}
#随机生成信息
class RandIfo(object):
    def __init__(self, idx):
        self.mates = []
        self.id = idx
        idx = 0
        while idx < 140:
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
             
#==========================myheap class=============================
class MaxHeap(object): 
    def __init__(self): 
        self._data = [] 
        self._count = len(self._data) 

    def size(self): 
        return self._count 
        
    def isEmpty(self): 
        return self._count == 0 

    def add(self, item): # 插入元素入堆 
        self._data.append(item) 
        self._count += 1 
        self._shiftup(self._count-1) 
        
    def pop(self): # 出堆 
        if self._count > 0: 
            ret = self._data[0] 
            self._data[0] = self._data[self._count-1] 
            self._data.pop()
            self._count -= 1 
            self._shiftDown(0) 
            return ret 
    
    def _shiftup(self, index): # 上移self._data[index]，以使它不大于父节点 
        parent = (index-1)>>1
        while index > 0 and self._data[parent] < self._data[index]: 
            # swap 
            self._data[parent], self._data[index] = self._data[index], self._data[parent] 
            index = parent 
            parent = (index-1)>>1 
    
    def _shiftDown(self, index): # xia移self._data[index]，以使它不小于子节点 
        j = (index << 1) + 1 
        while j < self._count : 
            # 有子节点 
            if j+1 < self._count and self._data[j+1] > self._data[j]: 
                # 有右子节点，并且右子节点较大 
                j += 1 
            if self._data[index] >= self._data[j]: # 堆的索引位置已经大于两个子节点，不需要交换了 
                break 
            self._data[index], self._data[j] = self._data[j], self._data[index] 
            index = j 
            j = (index << 1) + 1 

#=========================bjutAdmit=================================
def bjutAdmit(stuHeapify, school):
    admitNum = 0
    for major in school.major:
        #计数
        admitNum += major.Majornum 
    while admitNum > 0 and stuHeapify.size() > 0:
        tmpStu = stuHeapify.pop()
        tmpWill = []
        for will in tmpStu.will:
            tmpWill.append(will)
        while tmpStu.isAdmit is False:                
            if len(tmpWill) == 0:
                #所报志愿均满员
                retryHeap.add(tmpStu)
                break
            else:           
                op = tmpWill.pop(0)
                for major in school.major:
                    if op == major.Majorcode and major.Majorless > 0:
                        tmpStu.isAdmit = True
                        major.add(tmpStu)
                        admitNum -= 1

#===============================gui=================================
#重写的多列listbox
class MultiListbox(Frame): 
    def __init__(self,master,lists): 
        Frame.__init__(self,master) 
        self.lists = [] 
        for l, w in lists: 
            frame = Frame(self) 
            frame.pack(side=LEFT, 
            expand=YES, fill=BOTH) 
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X) 
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0, relief=FLAT, exportselection=FALSE) 
            lb.pack(expand=YES, fill=BOTH) 
            self.lists.append(lb) 
            lb.bind("<B1-Motion>",lambda e, s=self: s._select(e.y)) 
            lb.bind("<Button-1>",lambda e,s=self: s._select(e.y)) 
            lb.bind("<Leave>",lambda e: "break") 
            lb.bind("<B2-Motion>",lambda e,s=self: s._b2motion(e.x,e.y)) 
            lb.bind("<Button-2>",lambda e,s=self: s._button2(e.x,e.y)) 
        frame = Frame(self) 
        frame.pack(side=LEFT, fill=Y) 
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X) 
        sb = Scrollbar(frame,orient=VERTICAL, command=self._scroll) 
         
        self.lists[0]["yscrollcommand"] = sb.set 
        sb.pack(side=LEFT, fill=Y)
    
    def _select(self, y): 
        row = self.lists[0].nearest(y) 
        self.selection_clear(0, END) 
        self.selection_set(row) 
        return "break" 
    
    def _button2(self, x, y): 
        for l in self.lists: 
            l.scan_mark(x,y) 
        return "break" 
    
    def _b2motion(self, x, y): 
        for l in self.lists: 
            l.scan_dragto(x, y) 
        return "break" 
    
    def _scroll(self, *args): 
        for l in self.lists: 
            l.yview(*args)
        return "break" 
    
    def curselection(self): 
        return self.lists[0].curselection() 
    
    def delete(self, first, last=None): 
        for l in self.lists: 
            l.delete(first,last) 
        
    def get(self, first, last=None): 
        result = [] 
        for l in self.lists: 
            result.append(l.get(first,last)) 
        if last: 
            return apply(map, [None] + result) 
        return result 
    
    def index(self, index): 
        self.lists[0],index(index) 
    
    def insert(self, index, *elements): 
        for e in elements: 
            i = 0 
            for l in self.lists: 
                l.insert(index, e[i]) 
                i = i + 1 
    
    def size(self): 
        return self.lists[0].size() 
    
    def see(self, index): 
        for l in self.lists:
            l.see(index) 
    
    def selection_anchor(self, index): 
        for l in self.lists: 
            l.selection_anchor(index) 
            
    def selection_clear(self, first, last=None): 
        for l in self.lists: 
            l.selection_clear(first,last) 
    
    def selection_includes(self, index): 
        return self.lists[0].seleciton_includes(index) 
    
    def selection_set(self, first, last=None): 
        for l in self.lists: 
            l.selection_set(first, last) 

#窗口创建
class CreatWindow(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.ceratWidgets()
        messagebox.showinfo("Message","Welcome!") #弹出消息窗口
    
    def ceratWidgets(self):
        #框架布局
        self.Msgframe = LabelFrame(root, height = 670, width = 1590, text = 'information', padx = 10, pady = 10)
        self.Msgframe.pack_propagate(0)
        self.Msgframe.pack()                        
        self.Cmdframe = LabelFrame(root, height = 220, width = 1590, text = 'command', padx = 10, pady = 10)
        self.Cmdframe.pack_propagate(0)
        self.Cmdframe.pack()                                   

        #information--------列表框
        self.listbox0 = MultiListbox(self.Msgframe, [['INFORMATION',10]])
        self.listbox0.pack(expand=YES, fill=BOTH, side = LEFT)
        self.listbox1 = MultiListbox(self.Msgframe, (('ID', 5), ('Name', 5), ('Age', 3), ('sex', 6), ('Total', 5), ('Chinese', 5), ('Math', 5), ('English', 5), ('Comp', 5), ('Will', 20)))      
        self.listbox1.pack(expand=YES, fill=BOTH, side = RIGHT)
        #command------------button
        self.btn0 = Button(self.Cmdframe, text = 'School\nInformation', width = 15, height = 5, command = self.btn0Inf)
        self.btn0.grid(row = 0,column = 0, padx = 40, pady = 60)        
        self.btn1 = Button(self.Cmdframe, text = 'Student\nInformation', width = 15, height = 5, command = self.btn1Inf)
        self.btn1.grid(row = 0,column = 1, padx = 40, pady = 60)       
        self.btn2 = Button(self.Cmdframe, text = 'Preliminary\nResults', width = 15, height = 5, command = self.btn2Inf, state = DISABLED)
        self.btn2.grid(row = 0,column = 2, padx = 40, pady = 60)
        self.btn3 = Button(self.Cmdframe, text = 'Dispensing\nStudent', width = 15, height = 5, command = self.btn3Inf, state = DISABLED)
        self.btn3.grid(row = 0,column = 3, padx = 40, pady = 60)
        self.btn4 = Button(self.Cmdframe, text = 'Retired\nStudent', width = 15, height = 5, command = self.btn4Inf, state = DISABLED)
        self.btn4.grid(row = 0,column = 4, padx = 40, pady = 60)
        self.btn5 = Button(self.Cmdframe, text = 'Result\nof\nAdmission', width = 15, height = 5, command = self.btn5Inf, state = DISABLED)
        self.btn5.grid(row = 0,column = 5, padx = 40, pady = 60)
        self.btn6 = Button(self.Cmdframe, text = 'Exit', width = 15, height = 5, command = root.quit).grid(row = 0,column = 6, padx = 20, pady = 60) 
    
    def btn0Inf(self): 
        self.listbox0.delete(0, END)
        self.listbox0.insert(END, ['SchoolCode:%s' %bjut.schCode], ['SchoolName:%s' %bjut.schName], ['MajorInformation:'], ['    code:name,num'])
        for major in bjut.major:
            self.listbox0.insert(END, ['    %s:%s,%s'%(major.Majorcode, major.Majorname, major.Majornum)])    
        messagebox.showinfo("Message","Operation succeeded!") #弹出消息窗口
        
    def btn1Inf(self):       
        self.btn2['state'] = 'normal'
        self.btn3['state'] = 'normal'
        self.btn4['state'] = 'normal'
        self.btn5['state'] = 'normal'
        
        self.listbox1.delete(0, END)
        for student in myClass.mates:
            self.listbox1.insert(END, student.strIfo())
        messagebox.showinfo("Message","Operation succeeded!") #弹出消息窗口        

    def btn2Inf(self):
        self.listbox0.delete(0, END)
        self.listbox1.delete(0, END)
        
        for major in bjut.major:
            self.listbox0.insert(END, ['Majorcode:%s' %major.Majorcode], ['Majorname:%s' %major.Majorname], ['less:%s' %major.Majorless], [''])
            for student in major.mates:
                tmplist = student.strIfo()
                tmplist.pop()
                tmplist.append(str('%s' %major.Majorcode))
                self.listbox1.insert(END, tmplist)
        
        messagebox.showinfo("Message","Operation succeeded!") #弹出消息窗口       

    def btn3Inf(self):
        self.listbox1.delete(0, END)
        for student in retryHeap._data:
            self.listbox1.insert(END, student.strIfo())  
        messagebox.showinfo("Message","Operation succeeded!") #弹出消息窗口       

    def btn4Inf(self):
        self.listbox1.delete(0, END)
        for student in tmpHeap._data:
            self.listbox1.insert(END, student.strIfo())      
        messagebox.showinfo("Message","Operation succeeded!") #弹出消息窗口        
    
    def btn5Inf(self):
        self.listbox0.delete(0, END)
        self.listbox1.delete(0, END)
        
        for major in bjut.major:
            self.listbox0.insert(END, ['Majorcode:%s' %major.Majorcode], ['Majorname:%s' %major.Majorname], ['less:%s' %major.Majorless], [''])
            for student in major.mates:
                tmplist = student.strIfo()
                tmplist.pop()
                tmplist.append(str('%s' %major.Majorcode))
                self.listbox1.insert(END, tmplist)
    
        messagebox.showinfo("Message","Operation succeeded!") #弹出消息窗口               
#===============================main================================
if __name__ == '__main__':  
    bjut = SchIfo(1049, 'bjut')
    myClass = RandIfo('2018')
    
    retryHeap = MaxHeap()
    tmpHeap = MaxHeap()
    for student in myClass.mates:
       tmpHeap.add(student)
    bjutAdmit(tmpHeap, bjut)

    root = Tk()
    root.title('学生志愿管理系统')
    #设置窗口大小
    width = 1600
    height = 900
    #设置居中
    screenwidth = root.winfo_screenwidth() 
    screenheight = root.winfo_screenheight() 
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2) 
    root.geometry(alignstr)
    #设置窗口不可变
    root.resizable(width = False, height = False)

    app = CreatWindow(master = root)
    app.mainloop()