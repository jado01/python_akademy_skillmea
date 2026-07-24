from modules.employee import Employee
from modules.audit_log import save_log

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
            return f"Department {self.name} has no employee."
        lines =  [f"Employees in department {self.name}:"]
        for employee in self.employees:
            lines.append(f"- {employee.name} {employee.surname}")
        return "\n".join(lines)