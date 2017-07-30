import sys
print "You are applying the OR FUNCTION !" \
      "Please input two  binary or boolean lists." \
      "These lists must be same length and style!"

#input1_list =input("Here is the first  list:")
#input2_list =input("Here is the second list:")
input1_list=[False ,False ,True ,True ]
input2_list=[False ,True,False ,True ]

def or_gate(x,y):
    output = []
    for a,b in zip(x ,y ):
        output.append(a or b)
    print "OR logic output",output
    return output


def test_or():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert  or_gate(input1,input2) == [False,True,True,True]
    print "and Test Passed !"




test_or()
or_gate(input1_list,input2_list)
#Or([1,1,0],[0,1,0])