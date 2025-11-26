class Role:
    __next_user_general_id= 5000
    
    def __init__(self, fname, lname, age):
        self.__id = Role.__next_user_general_id
        Role.__next_user_general_id += 1
        self.__fname = fname
        self.__lname = lname
        self.__age = age
        self.__low_level_access = False
        self.__high_level_access = False
        self.__role = 'user'
    @property
    def id(self):
        return self.__id

    @property 
    def fname(self):
        return self.__fname
    @property
    def lname(self):
        return self.__lname

    @property
    def age(self):
        return self.__age

    @property
    def admin_role(self):
        self.__role = 'admin'
        return self.__role
    @property
    def dev_role(self):
        self.__role = 'dev'
        return self.__role

class Admin(Role):
    
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age)
        self.role = super().admin_role
    def grant_low_level_access(self,user):
        if self.role=='admin':
            user.low_level_access = True
            print('low_level_access granted!')
    def grant_high_level_access(self,user):
        if self.role == 'admin':
            user.high_level_access = True
            print('low_level_access granted!')
    def get_user_data(self,user):
        if self.role=="admin":
            print(f"Here is the user details:\n {user.fname} {user.lname} has {user.role} role and is {user.age} years old. Low-level-access: {user.low_level_access} | High-level-access: {user.high_level_access}")



class Dev(Role):
    
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname, age)
    def grant_low_level_access(self,user):
        if self.role=='dev':
            user.low_level_access = True
            print('low_level_access granted!')

class User(Role):
    
    def __init__(self, fname, lname, age,role):
        super().__init__(fname, lname, age,role)

ali = Admin('Ali', 'Jahankhah', '28', 'Admin')
print(ali.get_user_data(ali))

reza = User('Reza','Rezaei', '44','')