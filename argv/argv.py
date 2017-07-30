#coding=utf-8
import sys
from sys import argv
#将Python的特性（模块）引入脚本

script ,first ,second ,third = argv
#参数变量argument variable    unpack 解包l
print argv
print "the script is called ",script   #script 脚本，文件
x=raw_input("nice name")
print "the first variable is ：",first
y=raw_input("do you want to go on?")
print "the second variable is ： ",second
z=raw_input("you need one more value.")
print "the third variable is ：",third
#print "so,nice work.Go on!%r%r%r",%(first,second,third)

#  需要在terminal里先打开保存这个文件的文件夹，然后输入文件名.py  第一个变量名 第二个变量名 第三个变量名
#变量名可以随便取，
####   argv 和raw_input()的不同在于用户输入的时机，如果参数是在用户执行的命令的时候就要输入，那就argv，
#### 如果是在脚本运行过程中需要用户输入信息，那就用raw_input,我觉得raw_input更有人机互动感nice