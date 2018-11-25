f = open('/home/yanglin/homework/school information.txt', 'r')
for line in f.readlines():
    print(line.strip())
f.close()
f = open('/home/yanglin/homework/student information.txt', 'r')
for line in f.readlines():
    print(line.strip())
f.close()