ten_things ="Apples Orange Crows Telephone Light Suger"
print ten_things

print "Wait there's not 10 things in that list ,let's fix that."

stuff = ten_things.split()
print stuff
#separate the ten_things into list with comma
stuffs = ten_things.split(' ',3)
print stuffs

#  means that the ten_things will be parted into 4 parts with comma.

more_stuff =["Days","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]


while len(stuff) !=10:
    next_one =more_stuff.pop()
#next_one will has the thing that the last thing witch more_stuff just delete
#if there is 3 in bracket of pop,then the next_one will has the fourth thing of stuff,stuff lose it.
    print "Adding: ", next_one
    stuff.append(next_one)
# put the thing that next_one has now into the bottom of stuff list
    print "There's %d items now." %len(stuff)
#add element into stuff to make the stuff has ten things,
# the elements are took from behind of more_stuff one by one

print "There we go :",stuff
# show what the stuff has now.
print "Let's do some things with stuff."

print stuff[1]
#print the first thing of stuff,count from left to right
print stuff[-1]
#print the first thing of stuff,count from right to left
print stuff.pop()
# delete the last thing of the stuff list ,then print it .
print ' '.join(stuff)
# add space between each thing of stuff
print '#'.join(stuff[3:5])

# add '#'  between the fourth thing and the firth thing of stuff.




