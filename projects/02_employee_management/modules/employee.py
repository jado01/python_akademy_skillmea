from modules.audit_log import save_log

class Employee:
    _next_id = 1
    def __init__(self, name, surname, position, salary, employee_id = None):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        if employee_id is None:
            self.employee_id = Employee._next_id
            Employee._next_id += 1
        else:
            self.employee_id = employee_id
            if employee_id >= Employee._next_id:
                Employee._next_id = employee_id + 1

    def raise_salary(self, increase_amount):
        if not isinstance(increase_amount, int):
            raise TypeError("Amount must be a number")
        if increase_amount <= 0:
            raise ValueError("Amount must be > 0")
        old_salary = self.salary
        self.salary += increase_amount
        save_log(f"Salary increased for {self.name} {self.surname}: old salary {old_salary}, increase {increase_amount}, new salary {self.salary}.")

    def __str__(self):
        return f"ID: {self.employee_id} Name: {self.name} Surname: {self.surname} Position: {self.position} Salary: {self.salary}"

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Salary must be a number")
        if amount <= 0:
            raise ValueError("Salary must be > 0")
        self.__salary = amount
