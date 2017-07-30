import sys
import class_gates
from class_gates import gate
from class_gates import and_gate
from class_gates import nand_gate
from class_gates import  xor_gate
from class_gates import  xnor_gate
from class_gates import  not_gate
from class_gates import  or_gate
from class_gates import  nor_gate

input1 = [False, False, True, True]
input2 = [False, True, False, True]

binary(4)

def halfadd(a,b):
    sum=[]
    carry_in=[]
    s=xor_gate()
    sum.append(s.eval(a,b))
    c=and_gate()
    carry_in.append(c.eval(a,b))
    print  sum,carry_in
    #return sum,carry_in




halfadd(input1,input2)