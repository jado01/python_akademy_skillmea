from models.employee import Employee
from services.audit_log import save_log

class Manager(Employee):
    def add_employee_to_department(self, department, employee):
        if not isinstance(department, Department):
            raise TypeError("Department must be an instance of Department.")
        if department.manager is not self:
            raise ValueError("This manager does not manage this department.")
        department.add_employee(employee)

    @property
    def employee_type(self):
        return "manager"

class Department:
    def __init__(self, name, manager):
        if not isinstance(name, str):
            raise TypeError("Name of the department must be a string.")
        name = name.strip()
        if not name:
            raise ValueError("Name of the department cannot be empty.")
        self.name = name
        if not isinstance(manager, Manager):
            raise TypeError("Department manager must be an instance of Manager.")
        if name.isdigit():
            raise ValueError("Department name cannot contain only numbers.")
        self.manager = manager
        self.employees = []
        self.teams = []
    
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
            lines.append(f" - {employee.name} {employee.surname}")
        return "\n".join(lines)

    def create_team(self, name):
        new_team = Team(name)

        for team in self.teams:
            if team.name == new_team.name:
                raise ValueError("This team already exists.")

        self.teams.append(new_team)
        return new_team

    def list_teams(self):
        if not self.teams:
            return f"Department {self.name} has no teams."
        lines = [f"Department {self.name} has these teams:"]
        for team in self.teams:
            lines.append(f"- {team.name}")
        return "\n".join(lines)

    def add_employee_to_team(self, employee, team):
        if not isinstance(employee, Employee):
            raise TypeError("Employee must be an instance of Employee.")
        if not isinstance(team, Team):
            raise TypeError("Team must be an instance of Team.")
        if employee not in self.employees:
            raise ValueError("This employee is not from this department.")
        if team not in self.teams:
            raise ValueError("This team is not from this department.")
        team.add_member(employee)
        save_log(f"Employee {employee.name} {employee.surname} from department {self.name} added to the team {team.name}.")
            
class Leader(Manager):
    def __init__(self, name, surname, position, salary, employee_id=None):
        super().__init__(name, surname, position, salary, employee_id=employee_id)
        self.departments = []

    def add_department(self, department):
        if not isinstance(department, Department):
            raise TypeError("Only a Department instance can be added to the list of departments.")
        if department in self.departments:
            raise ValueError("Department is already in list.")
        self.departments.append(department)
        save_log(f"Department: {department.name} assigned to list of leader {self.name} {self.surname}.")

    def list_departments(self):
        if not self.departments:
            return f"Leader {self.name} {self.surname} has no departments."
        lines = [f"Leader {self.name} {self.surname} has these departments:"]
        for department in self.departments:
            lines.append(f" - {department.name}")
        return "\n".join(lines)

    @property
    def employee_type(self):
        return "leader"

class Team:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name of the team must be a string.")
        name = name.strip()
        if not name:
            raise ValueError("Name of the team cannot be empty.")
        self.name = name
        self.members = []

    def add_member(self, member):
        if not isinstance(member, Employee):
            raise TypeError("Only an Employee instance can be added to the team.")
        if member in self.members:
            raise ValueError("Member is already in the team.")
        self.members.append(member)

    def list_members(self):
        if not self.members:
            return f"Team {self.name} has no members."
        lines = [f"Team {self.name} has these members:"]
        for member in self.members:
            lines.append(f"- {member.name} {member.surname}")
        return "\n".join(lines)

