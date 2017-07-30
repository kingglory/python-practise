from sys import argv
from os.path import exists
#use import key to take exists function into this file

script,from_file,to_file=argv

print "Copying from %s to %s" %(from_file,to_file)

#we could do these two on one line too,how?
#in_file =open(from_file)
#indata = in_file.read()
in_file =open(from_file,'r+')

print"The input file is %d bytes long" %len(from_file)
print"Dose the output file exist?%r" %exists(to_file)
#if the to_file exist ,the result will be true;else ,false.
print"Ready,hit RETURN to continue ,CTRL-C to abort."
raw_input()

out_file =open(to_file,'w')
out_file.write(in_file)

print "Alright,all done."

out_file.close()
in_file.close()