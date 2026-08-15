import os

def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")
        
def pause():
    input("Press Enter to return to the main menu...")

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
    print("Available departments:\n")
    for number, department in enumerate(departments, start=1):
        print(f"  {number}. {department.name:<23}"
              f"  | Manager: {department.manager.name} {department.manager.surname}"
              )
    print()

    while True:
        try:
            chosen_number = int(input("Enter department number: "))
        except ValueError:
            print("\nPlease enter a valid number\n")
            continue

        if chosen_number in range(1, len(departments) + 1):
            return departments[chosen_number - 1]

        print("\nThis department doesn't exist.\n")

def select_team(department):
    print(f"Available teams in department {department.name}:\n")

    for number, team in enumerate(department.teams, start=1):
        print(f"  {number}. {team.name}")

    while True:
        try:
            chosen_number = int(input("\nEnter team number: "))
        except ValueError:
            print("\nPlease enter a valid number\n")
            continue

        if chosen_number in range(1, len(department.teams) + 1):
            return department.teams[chosen_number - 1]

        print("\nThis team doesn't exist.\n")

def select_employee(employees):
    print("Available employees:\n")
    for employee in employees:
        full_name = f"{employee.name} {employee.surname}"

        print(f"  ID: {employee.employee_id:<4}"
              f"| {full_name:<28}"
              f"| Position: {employee.position}"
              )
    print()

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
