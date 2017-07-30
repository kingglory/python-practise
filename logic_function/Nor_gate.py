import sys
print "You are applying the NOR FUNCTION !" \
      "Please input two  binary or boolean lists." \
      "These lists must be same length and style!"

def Nor(x,y):
    output = []
    for a,b in zip(x ,y):
        output.append(not(a or b))
    print "NOR logic output",output
    return output



Nor([1],[0])


#Nor([1,1,0],[0,1,0])