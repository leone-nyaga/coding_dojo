#!/usr/bin/python3

class SoftwareEngineer:
    alias = "Keyboard Warrior"

    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Level: {self.level}, Salary: {self.salary}"
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Level: {self.level}, Salary: {self.salary}"

    def entrySalary(self, age):
        if age < 25:
            return 50000
        if age < 35:
            return 75000
        else:
            return 100000

#instance(object)
se1 = SoftwareEngineer("Mike", 22, "Junior", 75000)
print(se1)
print(se1.alias)
print(SoftwareEngineer.alias)
se2 = SoftwareEngineer("Jane", 39, "Senior", 100000)
print(se2)
print(repr(se1))
print("Entry Salary: ", se1.entrySalary(se1.age))
