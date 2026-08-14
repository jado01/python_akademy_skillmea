from helpers import clear_terminal, pause
from services.data_storage import load_employees, load_departments
from actions import add_employee_to_team, add_employee_to_department, assign_department_to_leader
from actions import create_employee, create_department, create_leader, create_manager, create_team
from actions import increase_employee_salary, show_all_employees, show_departments, show_organization_structure
from actions import record_leader_decision

def run_menu():
    employees = load_employees()
    departments = load_departments(employees)

    while True:
        clear_terminal()
        print("""--== Employee management system ==--

Employee management
    1. Create new employee
    2. Create a new manager
    3. Increase an employee's salary
    4. Show all employees

Department and team management
    5. Create a new department
    6. Add an employee to a department
    7. Create a new team
    8. Add an employee to a team
    9. Show all departments

Organization and leader management
    10. Create a new leader
    11. Add department to leader
    12. Record a leader decision
    13. Show organization structure

    0. Exit
    """)

        while True:
            choice = input("Please choose an option: ")

            if choice.isdigit() and 0 <= int(choice) <= 13:
                break
            else:
                print("Invalid choice, please choose 1 - 13 or 0 for exit.")

        if choice == "1":
            create_employee(employees)

        elif choice == "2":
            create_manager(employees)
                
        elif choice == "3":
            increase_employee_salary(employees)

        elif choice == "4":
            show_all_employees(employees)

        elif choice == "5":
            create_department(employees, departments)

        elif choice == "6":
            add_employee_to_department(employees, departments)

        elif choice == "7":
            create_team(departments)

        elif choice == "8":
            add_employee_to_team(departments)

        elif choice == "9":
            show_departments(departments)

        elif choice == "10":
            create_leader(employees)

        elif choice == "11":
            assign_department_to_leader(employees, departments)

        elif choice == "12":
            record_leader_decision(employees)

        elif choice == "13":
            show_organization_structure(employees, departments)

        elif choice == "0":
            print("The program is over")
            break
