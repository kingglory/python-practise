#coding=utf-8     #  中文注释必备
import sys
#from decimal import *   # 高精度模块decimal
w=1.2222226766666666666666
round(2.5)
print round

print "welcome to our new program"
a=22
print "today is not 7yue : hao",a
print "today is not 7yue a hao"
print "today is not  7yue "+str(a)+" hao"
b=a-1
print b
c="a"+"1"
print c
d=str(a)+"1"
print d
f="22"
print f+str(a)
type (f)
print f
g=float(2.111)
print g
h=5.21
print h
family = ["mark","zhengmin","xuyanting","xuruiqin","wangwensong"]


for x in range(0,100,2):     #  从0数到100，间隔为2
    print str(x)+family[0],str(x+1)+family[1],str(x+2)+family[2],str(x+3)+family[3],str(x+4)+family[4]
    x=x+1

for x in range(0,100,5):              # 从0数到100，间隔为5
    print str(x)+family[0],str(x+1)+family[1],str(x+2)+family[2],str(x+3)+family[3],str(x+4)+family[4]
    x=x+1
#sys.exit()      # 程序运行遇到这组代码就停止

coord=[12,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,2312,321,1,2,2,3,3,2,213,123,34,5,54,4,3,3,332,22,43,23,4,212,23,2,23]
for index,name in enumerate(family):
    print index,name

fancy_list=["wangwensong",26,"wangwenlong",19,"wangguanglin",13]
fancy_list.sort()
print fancy_list
coord.sort()
print coord
for id ,thing in enumerate(fancy_list):   # enumerate 将列表排序，并每个元素之前有序列号码，id和thing可以随便设定
    print id,thing

for bilibili ,haizeiwang in enumerate(family):
    print bilibili,haizeiwang


def wangwensong (str):
    print str("today is a nice day!")
    return
print "I am very happy,wangwensong()"
print "I am very happy,"
print wangwensong(str)
print wangwensong(str),"I am very happy!"
if family is not None:
    print"you can use it"
else:
    print "you can't use it"
l=None
if l is not None:
    print"you can use it"
else:
    print "you can't use it"

l=[True,True,False,False,True]
l.append(False)     # 给数组l添加一个元素False

for o in range(0,100,3):
    print o
print h
print l
family.append("wws")
print family
family.sort()    # 对family数组进行排序
print family
