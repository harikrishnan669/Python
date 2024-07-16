#__init__ method is to initialize (or assign values) the data members of a class when an object of that class is created
# “self” is used to access and manipulate the instance variables and methods within a class.
class students:
  year=2020     #static keyword
  def __init__(self,name,age,branch):      # defining a constructor
    self.name=name              # self will give the instances and get the values of each
    self.age=age
    self.branch=branch

  def add_age(self):
    self.age=self.age+1


  def display(self):
    print("year "+ str(students.year))
    print("Name "+ self.name)
    print("Age "+ str(self.age))
    print("branch "+ self.branch)

  @classmethod
  def add_year(cls):
    cls.year=cls.year+1

x=students("hari",20,"cse")
y=students("ravi",20,"cse")

x.display()
y.display()

print("---------------------------------------")
students.year=students.year+1

x.add_age()
y.add_age()

x.display()
y.display()

print("---------------------------------------")
students.add_year()

x.display()
y.display()

  
