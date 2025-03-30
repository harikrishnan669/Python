# The add operation is replaced by the add function so firstname goes to self.name and secondname goes to other.name
class sample:
  def set_name(self,name):
    self.name=name

  def __add__(self,other):
    name=self.name+other.name
    return name

first_name=sample()
second_name=sample()

first_name.set_name("Hari")
second_name.set_name("krishnan")

full_name=first_name+second_name
print(full_name)
