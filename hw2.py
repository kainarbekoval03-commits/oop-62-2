class Employee:
    def __init__(self, name, salary):
        self.get_salary = salary
        self.get_info = name

    def get_salary(self):
        return self.get_salary

    def get_role(self):
        return "Employee"

    def get_info(self):
        return f"Имя: {self.get_info()} | Роль: {self.get_role()} | Зарплата: {self.get_salary()}"


emp = Employee("Alex", 30000)
print(emp)





class BackendDevelope(Employee):
    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level

    def get_salary(self):
        if self.level == "middle":
            return int(self.salary * 1.2)
        elif self.level == "senior":
            return int(self.salary * 1.5)
        return self.salary

    def get_role(self):
        return f"BackendDevelope({self.level})"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_salary(self):
        return self.salary + self.team_size * 1000

    def get_role(self):
        return "Manager"


class Intern(Employee):
    def __init__(self, name, salary, months):
        super().__init__(name, salary)
        self.months = months

    def get_salary(self):
        return 10000

    def get_role(self):
        return "Intern"

    dev = BackendDevelope("Alex", 50000, "senior")
    mgr = Manager("Olga", 60000, 5)
    intern = Intern("Max", 20000, 3)

    print(dev.get_info())
    print(mgr.get_info())
    print(intern.get_salary())



employees = [
    BackendDeveloper("Artem", 40000, "middle"),
    Manager("Oleg", 50000, 5),
    Intern("Ivan", 20000, 3),
]

