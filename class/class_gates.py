class gate(object):
    def __init__(self):
        pass
        print "Abstract parent gate"

    def eval(self):
        pass


class and_gate(gate):
    def __init__(self,):
        print "AND gate constructed"

    def eval(self,x, y):
        output = []
        assert len(x) == len(y)
        for a, b in zip(x, y):
            assert type(a) == type(b)  # assert same type?
        for a, b in zip(x, y):
            output.append(a and b)
        print "AND logic output:",output
        return output

class or_gate(gate):
    def __init__(self):
        gate.__init__(self)
        print "OR gate constructed"


    def eval(self,x, y):
        output = []
        for a, b in zip(x, y):
            output.append(a or b)
        print "OR logic output", output
        return output


class nor_gate(gate):
    def __init__(self):
        gate.__init__(self)
        print " NOR gate constructed"

    def eval(self,x, y):
        output = []
        for a, b in zip(x, y):
            output.append(not (a or b))
        print "NOR logic output", output
        return output


class nand_gate(gate):
    def __init__(self):
        gate.__init__(self)
        print "NAND gate constructed"

    def eval(self,x, y):
        output = []
        for a, b in zip(x, y):
            output.append(not (a and b))
        print "Nand logic output", output
        return output


class not_gate(gate):
    def __init__(self):
        gate.__init__(self)
        print "first in child"
        print "NOT gate constructed"

    def eval(self,x):
        output = []
        for a in x:
            output.append(not (a))
        print "Not logic output", output


class xor_gate(gate):
    def __init__(self):
        gate.__init__(self)
        print "XOR gate constructed"

    def eval(self,x, y):
        output = []
        for a, b in zip(x, y):
            output.append(a ^ b)
        print "XOR logic output:", output
        return output

class xnor_gate(gate):
    def __init__(self):
        #gate.__init__(self)
        print "XNOR gate constructed"

    def eval(self,x, y):
        output = []
        for a, b in zip(x, y):
            output.append(not (a ^ b))
        print "XNOR logic output:", output
        return output

