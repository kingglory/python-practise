# coding=utf-8
import numpy
import sys

f=[1,1,1,1,]
a=[0,0,1,1]
b=[0,1,0,1]
a_array=numpy.array(a)
b_array=numpy.array(b)
f_array=numpy.array(f)
c_array=a_array+b_array
print c_array

#***********************************************
#   the upside code is wrong,the followed maybe right.
l=[0,0,1,1]
k=[0,1,0,1]
h=[1,1,1,1]
for x in range(0,4):
    h[x]=(l[x] or k[x])

print h