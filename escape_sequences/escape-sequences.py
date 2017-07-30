#coding=utf-8
import sys

tabby_cat ="\tI'm tabbed in"   #tabbed 分页
persian_cat ="I'm split\non a line."
backslash_cat ="I'm \\a\\cat."

fat_cat  ="""
I'll do a list:
    * Cat food
  \t* fishies
\t* Catnip\n\t* Grass
"""
# \t 水平制表符（TAB），相当于四个空格的缩进，第一个与第二个有两个空格的间隔，但结果仍然对其666
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "there are %s" %fat_cat
print "there are %r" %fat_cat
# %s打印的是你作为用户看到的东西，%r打印的是你作为程序员看到的东西









while True:
    for i in ["/","—","|","\\","|"]:
        print "%s\r"%i
sys.exit()
# \r 相当于回车键