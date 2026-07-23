import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "employee_management.log"

def save_log(message):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="UTF-8") as f:
        f.write(f"[{time_stamp}] {message}\n")

class Employee:
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def raise_salary(self, increase_amount):
        if not isinstance(increase_amount, int):
            raise TypeError("Amount must be a number")
        if increase_amount <= 0:
            raise ValueError("Amount must be > 0")
        old_salary = self.salary
        self.salary += increase_amount
        save_log(f"Salary increased for {self.name} {self.surname}: old salary {old_salary}, increase {increase_amount}, new salary {self.salary}.")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nPosition: {self.position}\nSalary: {self.salary}"
    
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

class Manager(Employee):
    def add_employee_to_department(self, department, employee):
        if not isinstance(department, Department):
            raise TypeError("Department must be an instance of Department.")
        if department.manager is not self:
            raise ValueError("This manager does not manage this department.")
        department.add_employee(employee)

class Department:
    def __init__(self, name, manager):
        self.name = name
        if not isinstance(manager, Manager):
            raise TypeError("Department manager must be an instance of Manager")
        self.manager = manager
        self.employees = []
    
    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError(f"Only an Employee instance can be added to department {self.name}")
        if employee in self.employees:
            raise ValueError(f"Employee is already in department {self.name}")
        self.employees.append(employee)
        save_log(f"Employee: {employee.name} {employee.surname}, position: {employee.position}, added to department: {self.name}.")

    def list_employees(self):
        if not self.employees:
            raise f"Department {self.name} has no employee."
        lines =  [f"Employees in department {self.name}:"]
        for employee in self.employees:
            lines.append(f"- {employee.name} {employee.surname}")
        return "\n".join(lines)

def main():
    e1 = Employee("Janko", "Mrkvicka", "Technician", 2000)
    e2 = Employee("Martina", "Vesela", "Economist", 2400)
    m1 = Manager("Martin", "Konecny", "Manager", 3000)
    d1 = Department("HR", m1)
    m2 = Manager("Peter", "Mokry", "Manager", 3100)
    d2 = Department("Tech", m2)

    m1.add_employee_to_department(d1, e2)
    print(d1.list_employees())

if __name__ == "__main__":
    main()
