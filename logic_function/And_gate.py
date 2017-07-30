import sys
import types

def and_gate(x, y):
    output = []
    assert len(x) == len(y)  #i did
    for a,b in zip(x,y):
          assert type(a)  == type(b)  #assert same type?
    for a,b in zip(x ,y):
         output.append(a and b)
    print output
    return output


def test_and():
    input1 = [False, False, True, True]
    input2 = [False, True, False, True]
    assert  and_gate(input1,input2) == [False,False,False,True]
    print "and Test Passed !"
print "You are applying the AND FUNCTION !\n" \
      "Please input two  binary or boolean lists.\n" \
      "These lists must be same length and type!"

#input1_list =input("Here is the first  list:")
#input2_list =input("Here is the second list:")
test_and()
#and_gate(input1_list, input2_list)
and_gate([1,0,1,1],[True,False,True,True ])

