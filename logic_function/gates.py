import types


def and_gate(x, y):
    output = []
    assert len(x) == len(y)  #i did
    for a,b in zip(x,y):
        assert type(a) == type(b)
    for a,b in zip(x ,y):
         output.append(a and b)
    print output
    return output


def nand_gate(x, y):
    output = []
    assert len(x) == len(y)
    for a,b in zip(x,y):
          assert type(a)  == type(b)
    for a,b in zip(x ,y):
         output.append(not(a and b))
    print "And logic output",output
    return output




def or_gate(x, y):
    output = []
    assert len(x) == len(y)
    for a,b in zip(x,y):
          assert type(a)  == type(b)
    for a, b in zip(x, y):
        output.append(a or b)
    print "OR logic output", output
    return output


def nor_gate(x,y):
    output = []
    assert len(x) == len(y)
    for a,b in zip(x,y):
          assert type(a)  == type(b)
    for a,b in zip(x ,y):
        output.append(not(a or b))
    print "NOR logic output",output
    return output


def not_gate(input1):
    output = []

    for a in input1:
        output.append(not(a))
    print "Not logic output",output
    print output

def xor_gate(x,y):
    output = []
    assert len(x) == len(y)
    for a,b in zip(x,y):
          assert type(a)  == type(b)
    for a,b in zip(x,y):
        output.append(a ^ b)
    print "XOR logic output:",output
    return output

def xnor_gate(x,y):
    output = []
    assert len(x) == len(y)
    for a,b in zip(x,y):
          assert type(a)  == type(b)
    for a,b in zip(x,y):
        output.append(not(a ^ b))
    print "XNOR logic output:",output
    return output


def test_xnor():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert  xnor_gate(input1,input2) == [True,False,False,True]
    print "xnor Test Passed !"





def test_xor():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert  xor_gate(input1,input2) == [False,True,True,False]
    print "xor Test Passed !"




def test_not():
    input = [False, False, True, True]
    not_gate(input) == [ True, True, False, False]
    print "not Test Passed !"






def test_and():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert  and_gate(input1,input2) == [False,False,False,True]
    print "and Test Passed !"


def test_or():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert or_gate(input1, input2) == [False, True, True, True]
    print "or Test Passed !"

def test_nand():
    input1 = [False, False, True, True]
    input2 =[False ,True,False ,True ]
    assert nand_gate(input1, input2) == [True , True , True , False]
    print "nand_gate passed!"


def test_nor():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert nor_gate(input1, input2) == [ True,False,False,False ]
    print "nor Test Passed !"


test_xor()
test_and()
test_or()
test_nand()
test_nor()
test_xnor()
test_not()

input1 = [False, False, True, True]
input2 = [False, True, False, True]
print "Please input two  binary or boolean lists.\n" \
       "These lists must be same length and type!"
#input1=input("First list:")
#input2=input("Second list:")
assert len(input1) == len(input2)
for a, b in zip(input1,input2):
    assert type(a) == type(b)
print "witch gate would you like to choose?" \
    "and?  or?  nand?  nor?  not?  xor?  xnor?"
x=raw_input()

if x == "and":
    and_gate(input1, input2)
elif x =="or":
    or_gate(input1, input2)
elif x == "nand":
    nand_gate(input1, input2)
elif x == "nor":
    nor_gate(input1, input2)
elif x == "not":
    not_gate(input1)
elif x == "xor":
    xor_gate(input1, input2)
elif x== "xnor":
    xnor_gate(input1, input2)
