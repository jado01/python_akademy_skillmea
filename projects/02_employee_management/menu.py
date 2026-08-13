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
    1. Create new employee
    2. Show all employees
    3. Increase an employee's salary
    4. Create a new manager
    5. Create a new department
    6. Show all departments.
    7. Add an employee to a department
    8. Create a new team
    9. Add an employee to a team
    10. Show organization structure
    11. Create a new Leader
    12. Add department to leader
    13. Record a leader decision
    14. Exit
    """)

        choice = input("Please choose an option: ")

        if choice == "1":
            create_employee(employees)

        elif choice == "2":
            show_all_employees(employees)
                
        elif choice == "3":
            increase_employee_salary(employees)

        elif choice == "4":
            create_manager(employees)

        elif choice == "5":
            create_department(employees, departments)

        elif choice == "6":
            show_departments(departments)

        elif choice == "7":
            add_employee_to_department(employees, departments)

        elif choice == "8":
            create_team(departments)

        elif choice == "9":
            add_employee_to_team(departments)

        elif choice == "10":
            show_organization_structure(employees, departments)

        elif choice == "11":
            create_leader(employees)

        elif choice == "12":
            assign_department_to_leader(employees, departments)

        elif choice == "13":
            record_leader_decision(employees)

        elif choice == "14":
            print("The program is over")
            break

        else:
            print("Invalid choice, please choose 1 - 14.")
            pause()
