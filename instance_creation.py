class students:
  year=2020
  def __init__(self,name,age,branch):   #__init__ method is to initialize (or assign values) the data members of a class when an object of that class is created
    self.name=name                      # “self” is used to access and manipulate the instance variables and methods within a class.

  def add_age(self):
    self.age=self.age+1


  def display(self):
    print("year "+ str(students.year))
    print("Name "+ self.name)
    print("Age "+ str(self.age))
    print("branch "+ self.branch)

x=students("hari",20,"cse")
y=students("ravi",20,"cse")

x.display()
y.display()

students.year=students.year+1

x.add_age()
y.add_age()

x.display()
y.display()
