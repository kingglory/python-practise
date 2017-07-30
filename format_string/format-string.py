#coding=utf-8
import sys
my_name = 'zed A. Shaw'
my_age =35 # not a lie
my_height = 74.65 # inches  英寸
my_weight = 180 # lbs 磅
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'brown'

#round(2.34,1)  此处是将2.34变为2.3，如果是近似小数位，近似为前一位最近的奇数，如果近似为整数则近似为最近的偶数。
#round(2.34,0) 近似完为2
print "Let's talk about %s."% my_name
print "he's %f inches tall."% my_height
print "he's %d pounds heavy."% my_weight
print "Actually that's not too  heavy."
#sys.exit()
print "he's teeyh are usually %r depending on the coffee."  %my_teeth    #老办法，在相应位置输入%d（整形）、
                                                                                 #%s（字符串形）、%f(浮点数）
                                                                                 # %r（什么都能输出）
                                                                                 #引号外加上%变量名


print "he's got %s eyes and %s hair."%(my_eyes ,my_hair )
print "he's teeyh are usually : depending on the coffee."  ,my_teeth      #  新的办法，在相应位置输入冒号，在引号外加逗号，
                                                                                 # 然后直接输入变量名
#This line is tricky ,try to get it exactly right
print "If I add %d, %d, and %d I got %d."%(my_age ,my_height ,my_weight ,my_age +my_height +my_weight )
# 在字符串中通过格式化字符放入多个变量“（milk，eggs，bread,soup)"