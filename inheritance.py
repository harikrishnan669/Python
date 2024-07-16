class Baseclass:
  def set_name(self,name):
    self.name=name

class Subclass(Baseclass):
  def display(self):
    print("Hellooo")

  def display_name(self):
    print("Name "+self.name)

x=Baseclass()
y=Subclass()
y.set_name("hari")
y.display()
y.display_name()
