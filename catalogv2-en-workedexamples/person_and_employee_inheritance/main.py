# Step1: Define the class
class Person():
        # Step 1.1: Initialize the attributes of the Person class.
        def __init__(self, name):
                self.name = name
        # Step 1.2: Define the method to return the person’s name
        def get_name(self):
                return self.name
        # Step 1.3: Define the method to return if the person is an employee
        def is_employee(self):
                return False
# Step2: Define a class that is Person’s child class or subclass
class Employee(Person):
        # Step 2.1: Define the method to return if the person is an employee
        def is_employee(self):
                return True
# Step3: Test the class
emp = Person("Melody")
print(emp.get_name(), emp.is_employee())
emp = Employee("Linda")
print(emp.get_name(), emp.is_employee())
