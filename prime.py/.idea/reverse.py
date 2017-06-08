class robot:
    __x=10
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def __str__(self):
        return "Name: "+self.name+" build year: "+str(self.year)+"   "+str(self.__x)
x=robot("marvel",2013)

y=str(x)
print(x)
print("Type of x is ",type(y))