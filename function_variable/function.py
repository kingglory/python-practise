def secret_formula(started):
    jeff_beans =started *500
    jar = jeff_beans/1000
    crates =jar/100
    return jeff_beans,jar,crates



starte_point=10000
beans,jar,crates =secret_formula(starte_point)
print "beans: %r jar:%s  crates:%d "  %(beans,jar,crates)


jar,beans,crates =secret_formula(starte_point)
print "beans  jar crates ",  beans,jar,crates


x,y,z =secret_formula(starte_point)
print "x  y   z ",  x,y,z

#So, the variable defined inside the function is temporary,
# and when the function returns, the return value can be given a variable