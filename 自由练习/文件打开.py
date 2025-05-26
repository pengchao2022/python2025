#注意 终端要切换到该目录下

f = open('myfile.txt')

for line in f:
    #找出以mm 开头的所有行
    if line.startswith('mm'):

        print(line)

   
for line in f:
    #找出以qq结尾的行
    if line.endswith('\n'):

        print(line)