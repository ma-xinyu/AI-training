class UserDAO:
    def __init__(self):
        self.users_data = ["yangqiang", "zhouyan", "zhangyuantong", "zhengli"]    
    
    def validate(self, username):
        return username.lower() in self.users_data