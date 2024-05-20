
class User:
    name: str
    email: str
    password: str
    confirm_password: str
    sign_in_login: str
    sign_in_password: str

    def __init__(self, name, email, password, confirm_password, sign_in_login, sign_in_password):
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.sign_in_login = sign_in_login
        self.sign_in_password = sign_in_password


user = User(
    'NARUTO',
    'jjriley4545@mail.ru',
    'jjrilenaruto777',
    'jjrilenaruto777',
    'kh4ydarovs@yandex.ru',
    'siera5795630',


)

