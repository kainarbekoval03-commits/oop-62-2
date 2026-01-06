class Employee:
    def __init__(self, name, salary):
        self.get_salary = salary
        self.get_info = name
        self.get_role = "Employee"

    def action(self):
        return f"Имя: {self.get_info} | Роль: {self.get_role} | Зарплата: {self.get_salary}"


class BackendDeveloper(Employee):
    def init(self, name, salary, level):
        super().init(name, salary)
        self.level = level

    def get_salary(self):
        if self.level == "middle":
            return int(self.salary * 1.2)
        elif self.level == "senior":
            return int(self.salary * 1.5)
        return self.salary  # junior

    def get_role(self):
        return "BackendDeveloper"


class Manager(Employee):
    def init(self, name, salary, team_size):
        super().init(name, salary)
        self.team_size = team_size

    def get_salary(self):
        return self.salary + self.team_size * 1000

    def get_role(self):
        return "Manager"


class Intern(Employee):
    def init(self, name, salary, months):
        super().init(name, salary)
        self.months = months

    def get_salary(self):
        return 10000

    def get_role(self):
        return "Intern"

    def print_salary(employees):
        for emp in employees:
            print(emp.get_info())

employees = [
    BackendDeveloper("Artem", 40000, "middle"),
    Manager("Oleg", 50000, 5),
    Intern("Ivan", 20000, 3),
]
print_salary(employees)
# print(emp.get_role)
# print(emp.get_salary)
# class BackendDeveloper:
