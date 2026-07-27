from modules.employee import Employee

def run_menu():
    employees = []

    while True:
        print("""--== Employee management system ==--
    1. Create new employee
    2. Show all employees
    3. Increase an employee's salary
    4. Exit
    """)

        choice = input("Please choose an option: ")

        if choice == "1":
            name = input("Enter a name: ")
            surname = input("Enter a surname: ")
            position = input("Enter a position: ")
            salary = int(input("Enter a salary: "))
            new_employee = Employee(name, surname, position, salary)
            employees.append(new_employee)

        elif choice == "2":
            if not employees:
                print("\nThere are no employees.\n")
            else:
                for employee in employees:
                    print(employee)
                
        elif choice == "3":
            if not employees:
                print("\nThere are no employees.\n")
            else:
                found_employee = None
                entered_id = int(input("Enter ID of employee: "))
                for employee in employees:
                    if employee.employee_id == entered_id:
                        found_employee = employee
                        break
                if found_employee is None:
                    print("There is no employee with this ID.")
                else:
                    confirmation = input(f"CONFIRMATION! This employe? {found_employee}? (y / n): ")
                    if confirmation == "y":
                        print("Salary will be increased.")
                    elif confirmation == "n":
                        print("Operation was canceled.")
                    else:
                        print("Invalid input.")

                    

        elif choice == "4":
            print("The program is over")
            break
        else:
            print("Invalid choice, please choose 1 - 4.")