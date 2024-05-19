
class User:
    name: str
    email: str
    password: str
    confirm_password: str

    def __init__(self, name, email, password, confirm_password):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password


user = User(
    'John',
    'szkhaydarov@gmail.com',
    'test1234567',
    'test1234567'

)

