from models.account import Account

class Users:
    def __init__(self,name, username,password):
        self.name=name
        self.username=username
        self.password=password
        self.account=Account(self)
        
