import sys
#print "please input one binary or boolean list."
#print not True
#print not False
#input1_list =input("Here is the  input1_list:")
#input1_list=[False ,False ,True ,True ]

def not_gate(x):
    output = []
    for a in x:
        output.append(not(a))
    print "Not logic output",output



def test_not():
    input = [False, False, True, True]
    #assert  not_gate(input) == [ True, True, False, False]
    print "not Test Passed !"

not_gate([1,1,1,0])
test_not()