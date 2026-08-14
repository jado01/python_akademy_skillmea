import os

def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")
        
def pause():
    input("Press Enter to return to the main menu....")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if not value:
            print("This field cannot be empty. Please try again.")
            continue

        if value.isdigit():
            print("This field cannot contain only numbers. Please try again.")
            continue

        return value

def select_department(departments):
    for department in departments:
        print(f"Department: {department.name}, Manager: {department.manager.name} {department.manager.surname}")

    while True:
        chosen_department = get_non_empty_input("Enter a name of department: ")

        for department in departments:
            if department.name.lower() == chosen_department.lower():
                return department

        print("This department doesn't exist.")

def select_team(department):
    print(department.list_teams())

    while True:
        chosen_team = get_non_empty_input("Enter a name of team: ")

        for team in department.teams:
            if team.name.lower() == chosen_team.lower():
                return team

        print("This team doesn't exist.")

def select_employee(employees):
    for employee in employees:
        print(employee)

    while True:
        try:
            chosen_employee_id = int(input("Enter ID of employee: "))
        except ValueError:
            print("ID must be a number.")
            continue

        for employee in employees:
            if employee.employee_id == chosen_employee_id:
                return employee

        print("Employee with this ID doesn't exist.")

def get_leaders(employees):
    leaders = []

    for employee in employees:
        if employee.employee_type == "leader":
            leaders.append(employee)
    return leaders
