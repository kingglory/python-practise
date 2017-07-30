## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self):
        print "Abstract parent animal."

#Comment

class Dog(Animal):

    def __init__(self,name):
        self.name = name

class Cat(Animal):

    def __init__(self,name):
        self.name = name


class person(object):

    def __init__(self,name):

        self.name = name

        ##persion has-a pet of some kid
        self.pet = None

class Employee(person):

    def __init__(self,name,salary):
        ##?? hmm what is this atrange magic?
        super(Employee,self).__init__(name)
        ##?the upper line means apply the parent'function--init.
        # The result is the same as {self.name=name}
        self.salary =salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


##rover is-a Dog, the following line is a instance of class Dog!
rover = Dog("Rover")

##??the  following line is a instance of class Cat
satan = Cat("Satan")

##??following line is a instance of class persion
mary =person("Mary")

##??following line is taking the pet feature from class mary(the child class of person)into satan
mary.pet =satan

##??following line is a instance of class Employee
frank = Employee("Frank",120000)

frank.pet =rover

##??following line is a instance of class Fish
flipper =Fish()

##??following line is a instance of class Salmon
crouse =Salmon()

##??following line is a instance of class Halibut
harry =Halibut()


