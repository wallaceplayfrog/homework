from tkinter import *
import tkinter.messagebox as messagebox

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

#框架布局
Msgframe = LabelFrame(root, 
                    height = 670, width = 1590, 
                    text = 'information', 
                    padx = 10, pady = 10)
Cmdframe = LabelFrame(root, 
                    height = 220, width = 1590, 
                    text = 'command', 
                    padx = 10, pady = 10)
#设置框架窗口大小不变                    
Msgframe.pack_propagate(0)
Cmdframe.pack_propagate(0)

#information--------列表框
listbox1 = Listbox(Msgframe, height = 100, width = 1570, selectmode="browse")
scrl = Scrollbar(Msgframe)
scrl.pack(side = RIGHT, fill = Y)
listbox1.configure(yscrollcommand = scrl.set)

#command------------button
button0 = Button(Cmdframe, text = 'School\nInformation', width = 15, height = 5).grid(row = 0,column = 0, padx = 20, pady = 60)
button1 = Button(Cmdframe, text = 'Student\nInformation', width = 15, height = 5).grid(row = 0,column = 1, padx = 20, pady = 60)
button2 = Button(Cmdframe, text = 'Preliminary\nResults', width = 15, height = 5).grid(row = 0,column = 2, padx = 20, pady = 60)
button3 = Button(Cmdframe, text = 'Dispensing\nStudent', width = 15, height = 5).grid(row = 0,column = 3, padx = 20, pady = 60)
button4 = Button(Cmdframe, text = 'Retired\nStudent', width = 15, height = 5).grid(row = 0,column = 4, padx = 20, pady = 60)
button5 = Button(Cmdframe, text = 'Result\nof\nAdmission', width = 15, height = 5).grid(row = 0,column = 5, padx = 20, pady = 60)
button6 = Button(Cmdframe, text = 'Exit', width = 15, height = 5, command = root.quit).grid(row = 0,column = 6, padx = 20, pady = 60)
  
listbox1.pack()
Msgframe.pack()
Cmdframe.pack()
root.mainloop()