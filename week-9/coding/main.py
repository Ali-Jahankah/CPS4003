class Role:
    __next_user_general_id= 5000
    
    def __init__(self, fname, lname, age, role='user'):
        self.__id = Role.__next_user_general_id
        Role.__next_user_general_id += 1
        self.__fname = fname
        self.__lname = lname
        self.__age = age
        self.__role = role.lower()
        self.__low_level_access = self.__role in ('dev','admin')
        self.__high_level_access = self.__role == 'admin'
    
    def test_access(self):
        if self.low_level_access:
            print('You have now acess to the repo')
            if self.high_level_access:
                print('Also you are an admin now')
            return
        print("You don't have access to the repo because you are a user. Ask Admin or Devs for an access")
        return
    @property
    def id(self): return self.__id
    
    @property 
    def fname(self): return self.__fname

    @property
    def lname(self): return self.__lname

    @property
    def age(self): return self.__age

    @property
    def role(self): return self.__role
    
    @property
    def low_level_access(self):
        return self.__low_level_access
    @low_level_access.setter
    def low_level_access(self, value):
        self.__low_level_access = bool(value)
    
    @property
    def high_level_access(self):
        return self.__high_level_access
    @high_level_access.setter
    def high_level_access(self, value):
        self.__high_level_access = bool(value)

class Admin(Role):
    
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age, role='admin')
    def grant_low_level_access(self,user):
        if self.role=='admin' and user.id != self.id :
            user.low_level_access = not user.low_level_access
            print(f"low_level_access {'granted' if user.low_level_access else 'removed'}!")
            return
    def grant_high_level_access(self,user):
        if self.role == 'admin' and self.id != user.id and user.role !='admin':
            user.high_level_access = True
            user.low_level_access = True
            print(f"high_level_access {'granted' if user.high_level_access else 'removed'}!")
    def get_user_data(self,user):
        if self.role=="admin":
            print(f"Here is the user details:\n {user.fname} {user.lname} has {user.role} role and is {user.age} years old. Low-level-access: {user.low_level_access} | High-level-access: {user.high_level_access}")
            return

class Dev(Role):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age,role="dev")
    def grant_low_level_access(self,user):
        if self.role=='dev' and user.id != self.id :
            user.low_level_access = not user.low_level_access
            print(f"low_level_access {'granted' if user.low_level_access else 'removed'}!")

class User(Role):
    def __init__(self, fname, lname, age,role='user'):
        super().__init__(fname, lname, age,role)

ali = Admin('Ali', 'Jahankhah', 28)
first_dev = Dev('dev', 'devil', 20)
second_dev = Dev('dev', 'java', 66)
third_dev = Dev('dev', 'Python', 44)
first_user = User('user', 'mr x', 77)
second_user = User('user', 'mr xyz', 55)

first_user.test_access()
ali.grant_low_level_access(first_user)
first_user.test_access()

# =============================== Below line gives an error unless a setter method be set up in Role class as the role property is set to private
first_user.role = 'admin'  #Error - comment the line to avoid getting an error
# ==================================

ali.grant_low_level_access(first_user)
first_user.test_access()
ali.grant_high_level_access(first_user)
first_user.test_access()
ali.get_user_data(first_user)