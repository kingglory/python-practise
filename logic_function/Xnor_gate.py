
#input1_list=[False ,False ,True ,True ]
#input2_list=[False ,True,False ,True ]


def xnor(x,y):
    output = []
    for a,b in zip(x,y):
        output.append(not(a ^ b))
    print "XNOR logic output:",output
    return output
xnor([1,0,1],[1,1,0])

