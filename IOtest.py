f = open('/home/yanglin/homework/school information.txt', 'r')
f_list = f.readline().strip().split()
SchoolCode = int(f_list[0])
SchoolName = f_list[1]
print(SchoolCode, SchoolName)
for line in f.readlines():
    print(line.strip().split())
f.close()

f = open('/home/yanglin/homework/student information.txt', 'r')
f_list1 = f.readlines()
while len(f_list1) > 0:
    print(f_list1.pop(0).strip().split())
    print(f_list1.pop(0).strip())
    print(f_list1.pop(0).strip().strip("[]").split(","))

f.close()