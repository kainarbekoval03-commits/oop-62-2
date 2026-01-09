class User:
    def __init__(self, name, _email, __passwort):
        self.name = name
        self.show_email = _email
        self.check_passwort = __passwort

    def show_email(self):
        print(f'Ваш email: {self.show_email}')

    def check_password(self, __password):
        if self.check_passwort == __password:
            return True
        else:
            return False


    def change_password(self, old_password, new_password):
            if self.check_password(old_password):
                self.__password = new_password
                print("Пароль успешно изменен")
            else:
                print("Неверный старый пароль")

user = User("Ardager", "test@mail.com", "1234")

print(user.name)
user.show_email()

print(user.check_password("1234"))   # True
print(user.check_password("0000"))   # False

user.change_password("1234", "abcd")


from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        print("Машина едет по дороге")

class Bicycle(Transport):
    def move(self):
        print("Велосипед едет по велодорошке")


car = Car()
bike = Bicycle()
car.move()
bike.move()
