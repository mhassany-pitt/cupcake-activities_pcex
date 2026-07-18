# Step1: Define the class
class Person():
        #Step 1.1: Initialize the attributes of the Person class.
        def __init__(self, name, idnumber):
                self.name = name
                self.idnumber = idnumber
        # Step 1.2: Define the method to print the person's name and id
        def display(self):
                print(self.name)
                print(self.idnumber)
# Step2: Define a class that is Person's child class or subclass
class Employee(Person):
        # Step 2.1: Initialize the attributes of the Employee class.
        def __init__(self, name, idnumber, salary, post):
                self.salary = salary
                self.post = post
                Person.__init__(self, name, idnumber)
        # Step 1.2: Define the method to print the person's salary and post
        def info(self):
                print(self.salary)
                print(self.post)
a = Employee('Rahul', 886012, 200000, 'Intern')
a.display()
a.info()
