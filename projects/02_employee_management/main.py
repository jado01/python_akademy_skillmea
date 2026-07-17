class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def raise_salary(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        self.salary += amount

    def __str__(self):
        return f"Name: {self.name}\nPosition: {self.position}\nSalary: {self.salary}"
    
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
    e1 = Employee("Janko Mrkvicka", "Technician", 2000)

    print(e1)
    e1.raise_salary(200)
    print(e1)

if __name__ == "__main__":
    main()
