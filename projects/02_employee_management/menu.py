import os
from modules.employee import Employee
from modules.data_storage import save_employees, load_employees


def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")
        
def pause():
    input("Press Enter to continue ...")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def run_menu():
    employees = load_employees()

    while True:
        clear_terminal()
        print("""--== Employee management system ==--
    1. Create new employee
    2. Show all employees
    3. Increase an employee's salary
    4. Exit
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
            print("The program is over")
            break
        else:
            print("Invalid choice, please choose 1 - 4.")
            pause()