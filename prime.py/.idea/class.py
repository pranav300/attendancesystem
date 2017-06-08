class Person(object):
    def __init__(self,first,last):
        # type: (object, object) -> object
        self.first=first
        self.last=last
    def __str__(self):
        return "first= "+self.first+" last= "+self.last
class Employer(Person):
    def __init__(self,first,last,id):
        super(Employer,self).__init__(first,last)
        self.id=id
    def __str__(self):
        return "first= "+self.first+" last= "+self.last+" id= "+self.id
x=Person("pranav","agarwal")
y=Employer("pranav","agarwal","321")
print(x.__str__())
print(y.__str__())


