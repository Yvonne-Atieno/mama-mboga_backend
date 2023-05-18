class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Login:
    def __init__(self):
        self.users = []
    
    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print("User registered successfully!")
    
    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return True
        print("Invalid username or password.")
        return False