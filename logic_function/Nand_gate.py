import sys
print "You are applying the NAND FUNCTION !" \
      "Please input two  binary or boolean lists." \
      "These lists must be same length and style!"

#input1_list =input("Here is the first  list:")
#input2_list =input("Here is the second list:")
input1_list=[False ,False ,True ,True ]
input2_list=[False ,True,False ,True ]


def nand_gate(x, y):
    output = []
    for a,b in zip(x ,y):
         output.append(not(a and b))
    print "And logic output",output
    return output


def test_nand():
    input1 = [False, False, True, True]
    input2 =[False ,True,False ,True ]
    assert nand_gate(input1, input2) == [True , True , True , False]
    print "nand_gate passed"


#Nand([1,0,1,1],[0,1,1,0])

