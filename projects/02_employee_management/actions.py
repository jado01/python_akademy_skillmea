from helpers import pause, get_non_empty_input
from models.employee import Employee
from models.organization import Manager
from services.data_storage import save_employees
from services.audit_log import save_log

def create_employee(employees):
    name = get_non_empty_input("Enter a name: ")
    surname = get_non_empty_input("Enter a surname: ")
    position = get_non_empty_input("Enter a position: ")

    while True:
        try:
            salary = int(input("Enter a salary: "))
            new_employee = Employee(name, surname, position, salary)
        except ValueError:
            print("Salary must by a number and higher then 0!")
            continue
        break

    employees.append(new_employee)
    save_employees(employees)
    save_log(f"{new_employee} created.")
    print(f"New employee with ID: {new_employee.employee_id} name: {new_employee.name}, surname: {new_employee.surname}, position: {new_employee.position}, salary: {new_employee.salary} created.")
    pause()

def show_all_employees(employees):
    if not employees:
        print("\nThere are no employees.\n")
    else:
        for employee in employees:
            print(employee)
    pause()

def increase_employee_salary(employees):
    if not employees:
        print("\nThere are no employees.\n")
    else:
        found_employee = None
        try:
            entered_id = int(input("Enter ID of employee: "))
            for employee in employees:
                if employee.employee_id == entered_id:
                    found_employee = employee
                    break
        except ValueError:
            print("ID must be a number!")
            pause()
            return

        if found_employee is None:
            print("There is no employee with this ID.")
        else:
            confirmation = input(f"CONFIRMATION! This employee? {found_employee}? (y / n): ").strip().lower()

            if confirmation == "y":
                old_salary = found_employee.salary

                while True:
                    try:
                        increase_amount = int(input("Enter the amount of the salary increase: "))
                        found_employee.raise_salary(increase_amount)
                    except ValueError:
                        print("Amount must be a number and higher then 0!")
                        continue
                    break
                save_employees(employees)
                print(f"Salary of {found_employee.name} {found_employee.surname} was increased by {increase_amount} from {old_salary} to {found_employee.salary}.")
            elif confirmation == "n":
                print("Operation was canceled.")
            else:
                print("Invalid input.")
    pause()

def create_manager(employees):
    name = get_non_empty_input("Enter a name: ")
    surname = get_non_empty_input("Enter a surname: ")
    position = get_non_empty_input("Enter a position: ")            

    while True:
        try:
            salary = int(input("Enter a salary: "))
            new_manager = Manager(name, surname, position, salary)
        except ValueError:
            print("Salary must by a number and higher than 0!")
            continue
        break

    employees.append(new_manager)
    save_employees(employees)
    save_log(f"{new_manager} created.")
    print(f"New manager with ID: {new_manager.employee_id} name: {new_manager.name}, surname: {new_manager.surname}, position: {new_manager.position}, salary: {new_manager.salary} created.")
    pause()