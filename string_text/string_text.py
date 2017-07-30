#coding=utf-8
import sys

x = "there are %d types of people."  %10  #第一次见数字可以在外面当参数与里面的%呼应
binary = "binary"# 二进制

do_not = "don't"
y = "those who know % s and those who %s." %(binary,do_not)# 一次呼应两个参数

print x
print y

print "I said :%r."%x
print  "I also said :%s."%y
# %r用来做调试（debug）比较好，因为他会显示变量的原始数据（raw data），而%s和其他的符号则是用来向用户显示输出的


hilarious = False    # hilarious欢闹的
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation  %hilarious
#  此处相当于print "Isn't that joke so funny?! %r" % hilarious

w = "this is the left side of..."
e ="a string with a right side."

print w+e






print "mary had a little lamb ."    # lamb  小羊羔
print "Its fleece was  white as %s."  %'slow'  # fleece羊毛   直接将字符串‘slow’与内部的%呼应，调入
print "and everywhere that mary went."
print "*"*10 #what'd do that?
#watch that comma at the end,try to removei it to see what happens
print 'cheese',    #有逗号输出cheese burger,没有逗号两个词分两行输出
print 'burger'






formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","there","four")
print formatter % (True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)
print formatter % (
    "I said this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# here's some new strange stuff,remember type it exactly.
days = "monday tuesday wednesday thursday friday saturday sunday"
months = "\nJanuary\nFebruary\nMarch\nApril\nMay\nJune\nJuly\nAugust"    #换行、\n


print "Here are the days:",days
print "Here are the months:",months

print """     
There's something going on here
    
With the three double-quotes
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 , or 6. 
"""
# """   """字符串



print "I am 6'2\" tall.\\"    # 将字符串中的双引号转义,打印一个\需要输入两个\
print 'I am 6\'s" tall.'     #将字符串中的单引号转义