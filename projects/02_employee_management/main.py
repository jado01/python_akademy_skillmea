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


def main():
    e1 = Employee("Janko", "Mrkvicka", "Technician", 2000)

    print(e1)
    e1.raise_salary(200)
    print(e1)

if __name__ == "__main__":
    main()
