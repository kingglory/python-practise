#coding=utf-8
from sys import argv

script ,user_name = argv     # 打开的时候只需在terminal里输入prompy.wangwensong即可
prompt ='>'

print "hi %s, I'm the %s script." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)     #prompt 提示符

print "Where do you live %s?" %user_name
lives =raw_input(prompt)

print "What kind of computer do you have?"
computer=raw_input(prompt)

print """
Alright,so you said %r about liking me.
you live in %r .Not sure where that is.
and you have a %r computer.nice.
""" %(likes,lives,computer)
