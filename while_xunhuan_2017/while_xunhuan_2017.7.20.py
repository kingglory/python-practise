#coding=utf-8   #什么都不输入的时候会运行wws（相邻的）文件，为什么？是因为他们在同一个project里面吗？
i = 0
numbers = []
while i < 6:
    print "at the top is :", i
    numbers.append(i)

    i = i +1
    print "Numbers now :",numbers
    print "At the bottom i is %d" % i


print "The numbers :"

for num in numbers:
    print num
