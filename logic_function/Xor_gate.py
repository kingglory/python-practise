print "Now you are applying the XOR FUNCTION !" \
      "Please input two  binary or boolean lists." \
      "These lists must be same length and style!"
#input1_list =input("Here is the first  list:")
#nput2_list =input("Here is the second list:")
#input1_list=[False ,False ,True ,True ]
#input2_list=[False ,True,False ,True ]


def xor(x,y):
    output = []
    for a,b in zip(x,y):
        output.append(a ^ b)
    print "XOR logic output:",output
    return output
xor([1,0,1],[1,1,0])
#xor(input1_list,input2_list)