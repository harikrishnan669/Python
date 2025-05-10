class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print("Employee ID:", self.emp_id)

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

m = Manager("Alice", 101, "HR")
m.display()
