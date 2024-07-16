# Method overriding
class Baseclass:
  def __init__(self):
    print("Base init")

  def set_name(self,name):
    self.name=name
    print("heloo")

class Subclass(Baseclass):
  def __init__(self):
    print("Subclass init")

  def setr_name(self,name):
    self.name=name
    print("Hello")

x=Baseclass()
y=Subclass()
y.set_name("Hari")
