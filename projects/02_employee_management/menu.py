import os
from models.employee import Employee
from models.organization import Manager, Department
from services.data_storage import save_employees, load_employees


def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")
        
def pause():
    input("Press Enter to continue ...")

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

def run_menu():
    employees = load_employees()
    departments = []

    while True:
        clear_terminal()
        print("""--== Employee management system ==--
    1. Create new employee
    2. Show all employees
    3. Increase an employee's salary
    4. Create a new manager
    5. Create a newe department
    6. Show all departments.
    7. Add an employee to a department
    8. Exit
    """)

        choice = input("Please choose an option: ")

        if choice == "1":
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
            print(f"New employee with ID: {new_employee.employee_id} name: {new_employee.name}, surname: {new_employee.surname}, position: {new_employee.position}, salary: {new_employee.salary} created.")
            pause()

        elif choice == "2":
            if not employees:
                print("\nThere are no employees.\n")
            else:
                for employee in employees:
                    print(employee)
            pause()
                
        elif choice == "3":
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
                    continue

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

        elif choice == "4":
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
            print(f"New manager with ID: {new_manager.employee_id} name: {new_manager.name}, surname: {new_manager.surname}, position: {new_manager.position}, salary: {new_manager.salary} created.")
            pause()

        elif choice == "5":
            managers = []

            for employee in employees:
                if isinstance(employee, Manager):
                    managers.append(employee)
            if not managers:
                print("You need at least one manager to create a new department.")
                pause()
                continue
            for manager in managers:
                print(manager)

            found_manager = None

            while True:
                try:
                    manager_id = int(input("Enter ID of manager: "))
                    for manager in managers:
                        if manager.employee_id == manager_id:
                            found_manager = manager
                            break
                except ValueError:
                    print("ID must be a number!")
                    pause()
                    continue

                if found_manager is None:
                    print("There is no manager with this ID. Please enter ID again.")
                else:
                    while True:
                        department_name = get_non_empty_input("Enter a department name: ")
                        existing_department = None
                        for department in departments:
                            if department.name.lower() == department_name.lower():
                                existing_department = department
                                break
                        if existing_department is not None:
                            print("This department already exist. Please try again")
                        else:
                            new_department = Department(department_name, found_manager)
                            departments.append(new_department)
                            print(f"New department {department_name} with manager {found_manager.name} {found_manager.surname} created")
                            break
                    break

            pause()

        elif choice == "6":
            if not departments:
                print("No departments to show.")
            else:
                for department in departments:
                    print(f"Department: {department.name}, Manager: {department.manager.name} {department.manager.surname}")
            pause()

        elif choice == "7":
            if not departments:
                print("You need at least one department before adding an employee.")
            else:
                available_employees = []
                for employee in employees:
                    if employee.employee_type == "employee":
                        available_employees.append(employee)
                if not available_employees:
                    print("There are no employees available to add.")
                else:
                    for department in departments:
                        print(f"Department: {department.name}, Manager: {department.manager.name} {department.manager.surname}")

                    while True:
                        found_department = None
                        chosen_department = get_non_empty_input("Enter a name of department: ")

                        for department in departments:
                            if department.name.lower() == chosen_department.lower():
                                found_department = department
                                break

                        if found_department is None:
                            print("This department doesn't exist.")
                        else:
                            print(f"Which employee you want to add to department {chosen_department}?")
                            for employee in available_employees:
                                print(employee)

                            while True:
                                try:
                                    chose_id = int(input("Enter ID of employee: "))
                                except ValueError:
                                    print("ID must be a number.")
                                    continue

                                chosen_employee = None
                                
                                for employee in available_employees:
                                    if chose_id == employee.employee_id:
                                        chosen_employee = employee
                                        break

                                if chosen_employee is None:
                                    print("There is no employee with this ID. Please try again.")
                                else:
                                    try:
                                        found_department.manager.add_employee_to_department(found_department, chosen_employee)
                                    except ValueError as error:
                                        print(error)
                                    else:
                                        print(f"Employee {chosen_employee.name} {chosen_employee.surname} added to department {found_department.name}")
                                        break
                            break
            pause()

        elif choice == "8":
            print("The program is over")
            break
        else:
            print("Invalid choice, please choose 1 - 8.")
            pause()