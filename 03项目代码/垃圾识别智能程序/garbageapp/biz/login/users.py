class UserDAO:
    def __init__(self):
        self.users_data = ["zhangjiawei", "maxinyu", "likang", "luoxiao"]    
    
    def validate(self, username):
        return username.lower() in self.users_data
        # lower:大小写转换  返回值是一个bool值