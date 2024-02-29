import random
import datetime

class Employee():
    """
    Base employee class
    """

    raise_amount = 1.04
    number_of_employee = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Employee.number_of_employee += 1

    def __repr__(self):
        return 'Emplyee("{}" , "{}", "{}")'.format(self.first_name, self.last_name, self.salary) 
    
    def __str__(self):
        return "{} - {}".format(self.get_full_name() , self.email)
    
    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        return None
    
    @property
    def email(self):
        if self.first_name and self.last_name:
            return self.first_name + "." + self.last_name + "@gmail.com"
        return None
    
    @get_full_name.setter
    def get_full_name(self, name):
        self.first_name, self.last_name = name.split(" ")

    @get_full_name.deleter
    def get_full_name(self):
        print(f"{self.get_full_name}  is deleted!")
        self.first_name = None
        self.last_name = None
         
    def raise_salary(self): 
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount 

    @classmethod
    def from_string(cls, employee_string):
        first_name, last_name, salary = employee_string.split("-")
        new_obj = cls(first_name, last_name, salary)
        return new_obj
    
    @staticmethod
    def  is_work_day(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True
    
class Devloper(Employee):
    """ 
    Developer class which inherits Employee
    """
    raise_amount = 1.10

    def __init__(self, first_name, last_name, salary, prog_language, framework):
        super().__init__(first_name, last_name, salary)
        self.prog_language = prog_language
        self.framework = framework
        
class Manager(Employee):
    """
    Manager class which inherits Wmployee
    """
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees  = employees

    def add_emplyee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("---> " + emp.get_full_name())

 
emp_1 = Devloper("Surafel", "Melaku", 4000, "python", "Django")
emp_2= Devloper("man", "killo", 7000, "java", "spring")
del emp_1.get_full_name 
print(emp_1.first_name)
print(emp_1.email)
print(emp_1.get_full_name)