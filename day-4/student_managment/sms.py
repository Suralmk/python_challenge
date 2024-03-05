from . connection import Students, Departments, Users
"""

    User:
        First Name
        Last Name
        Password
        Username
        role

        Methods: Authenticate
                 Menus, for specific role           
    Student:
        Methods: get_grade

    Staff:
        Methods: add_student, add_department, add_grade
                 update_student, update_department, update_grade
                 delete_student, delete_department, delete_grade
        
"""
#Implmentation of a console student managment Sysstem 
class User:
    def __init__(self, first_name, last_name,username, password, role):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = role
            
    def show_menus(self):
        pass

    def authenticate(self):
        pass
    
class Student(User):
    """
    are able to see their grade grade, department and Grade giver staff member
    by authenticating with their username and password
    """
    def __init__(self, first_name, last_name, username, password, role):
        super().__init__(first_name, last_name, username, password, role)

    def show_grade():
        pass

class Staff(User):
    """
    Staff members can add, delete and update new students, departments,  and students grade
    """
    def __init__(self, first_name, last_name, username, password, role):
        super().__init__(first_name, last_name, username, password, role)

