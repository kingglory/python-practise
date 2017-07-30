
from sys import argv
script ,filename =argv
# if you want to apply this file,just type the names of this file and the file that you want to open.
# The name of this file is get-file.py.
# The name of the file that you want to use is ex15_sample
txt = open(filename)
#this command will open the file witch name is the second name you typed bofore.
print "Here's your file %r :" %filename

print txt.read()
# then it will carry out -readding the content in this file.
print "try the filename again:"
file_again =raw_input(">")
#we will need to type the filename again

txt_again =open(file_again)
# The file will be opend again.

print txt_again.read()
# The file will be read again