#coding=utf-8





input1=[0, 0, 1, 1]
input2=[0, 1, 0, 1]
h=[]
for x in range(0,4):
    h.append((input1[x] and input2[x]))

print "output for AND:", h

# priority   not>and >or
input1=[0, 0, 1, 1]
input2=[0, 1, 0, 1]
h=[]
for x in range(0,4):                    #把4改成3结果会变成1,1,1，1
    h.append((not(input1[x] and input2[x])))      #此处不添加int（）输出结果为True，True，True，False
                                         #加上int（）之后变为了1，1,1,0

print "output for NAND:",h


inp1=[False,False,True,True]
inp2 = [False,True,False,True]
output=[]
for a,b in zip(inp1,inp2):
    output.append(a and b)
print "output for logic",output
