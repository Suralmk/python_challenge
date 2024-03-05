from  connection import Students, Departments, Users
import sys
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
def authenticate():
        print("Please Enter your username and password")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if Users.find_one({"username":username}, {"password" :password}) is not None:
            user = Users.find_one({"username":username, "password" :password})

            user_detail = {
                "is_authenticated" : True,
                "username" : user.get("username"),
                "first_name" : user.get("first_name"),
                "last_name" :user.get("last_name"),
                "role" : user.get("role")
            }
            return user_detail

        else:
            print("Authentication failed! Username or password error!")
            is_authenticated = False
            sys.exit()

class User:
    def __init__(self, first_name, last_name,username,role,is_authenticated,  password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = role
        self.is_authenticatd = is_authenticated
    
    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        return None
    
    def show_grade(self):
        print("4.0")

    def exit(self):
        sys.exit()
 
class Student(User):
    """
    are able to see their grade grade, department and Grade giver staff member
    by authenticating with their username and password
    """
    def __init__(self, first_name, last_name, username, role, is_authenticated, password=None):
        super().__init__(first_name, last_name, username, role, is_authenticated, password)

    def show_menus(self):
        while True:
            print(f"Hello {self.get_full_name}")
            print("""
           Student Menus:
              1: See Grade
              2: exit
            """)
            choice = input("Enter menu number!: ")
            if int(choice) not in range(1, 3):
                print("Please enter a valid choice")
                continue
            if choice == "1":
                self.show_grade()
                continue
            if choice == "2":
                self.exit()
                break

    def show_grade(self):
        print("4.0")

class Staff(User):
    """
    Staff members can add, delete and update new students, departments,  and students grade
    """
    def __init__(self, first_name, last_name, username, role, is_authenticated, password=None):
        super().__init__(first_name, last_name, username, role, is_authenticated, password)

    def show_menus(self):
        print(f"Hello {self.get_full_name}")
        print("""
            Student Menus:
              1: Add Student
              2: Update student
              3: Add student Grade
              4: Delete Student
              5: exit
            """)

if __name__ == "__main__":
    user_detail = authenticate()
    user = User(user_detail.get("first_name"), 
                user_detail.get("last_name"), 
                user_detail.get("username"), 
                user_detail.get("role"), 
                user_detail.get("is_authenticated"))
    
    if user_detail.get("role") == "stu":
        Student.show_menus(user)
    else:
        Staff.show_menus(user)