class gate(object):
    def __init__(self, name):
        self.name=name
        print "%s gate constructed!" %self.name

    def check_input(self,x,y):

        import types
        assert len(x) == len(y)
        for a, b in zip(x, y):
            assert type(a) == type(b)
        print " logic output:",self
        return (x,y)



class and_gate(gate):
    def __init__(self,name):
        super(and_gate,self).__init__(name)

    def eval(self,x, y):
          x,y = self.check_input(x,y)
          output = []
          for a, b in zip(x, y):
              output.append(a and b)
          print output
          return output

class or_gate(gate):
    def __init__(self,name):
        super(or_gate, self).__init__(name)


    def eval(self,x, y):
        output = []
        for a, b in zip(x, y):
            output.append(a or b)
        print output
        return output


class nor_gate(gate):
    def __init__(self,name):
        super(nor_gate, self).__init__(name)


    def eval(self,x, y):
        x, y = self.check_input(x, y)
        output = []
        for a, b in zip(x, y):
            output.append(not (a or b))
        print  output
        return output




class nand_gate(gate):
    def __init__(self,name):
        super(nand_gate, self).__init__(name)

    def eval(self,x, y):
        x, y = self.check_input(x, y)
        output = []
        for a, b in zip(x, y):
            output.append(not (a and b))
        print output
        return output



class not_gate(gate):
    def __init__(self,name):
        super(not_gate, self).__init__(name)

    def eval(self,x):
        x, y = self.check_input(x, y)
        output = []
        for a in x:
            output.append(not (a))
        print  output
        return output
class xor_gate(gate):
    def __init__(self,name):
        super(xor_gate, self).__init__(name)

    def eval(self,x, y):
        x, y = self.check_input(x, y)
        output = []
        for a, b in zip(x, y):
            output.append(a ^ b)
        print  output
        return output




class xnor_gate(gate):
    def __init__(self,name):
        super(xnor_gate, self).__init__(name)

    def eval(self,x, y):
        x, y = self.check_input(x, y)
        output = []
        for a, b in zip(x, y):
            output.append(not (a ^ b))
        print  output
        return output




input1 = [False, False, True, True]
input2 = [False, True, False, True]



for gate in [and_gate(name), or_gate(name), nand_gate(name), xnor_gate(name), xor_gate(name), nor_gate(name)]:
    gate.eval(input1, input2)