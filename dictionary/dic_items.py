marklab ={1:"mark",2:"zhengmin",4:"xuyanting",3:"wanglong",
          6:"wangwensong",5:"xuruiqin"}


print "The elements of marklab is in following:",marklab.items()


for number,name in marklab.items():
    print number,name

print "value=:",marklab.has_key(1)
print "value=:",marklab.has_key(7)









def fab(max):
   n, a, b = 0, 0, 1
   L = []
   while n < max:
       L.append(b)
       a, b = b, a + b
       n = n + 1
   return L



print fab(5)




class Thing(object):
    def test(self,name):
        self.name=name
        print self.name

a =Thing()
a.test('hello')