from helpers import clear_terminal, pause, get_non_empty_input, select_department, select_employee, select_team, get_leaders
from models.organization import Department, Leader
from services.data_storage import save_employees, load_employees, save_departments, load_departments
from services.audit_log import save_log
from actions import add_employee_to_team, add_employee_to_department, create_employee, create_manager, create_department, show_departments, create_team
from actions import increase_employee_salary, show_all_employees

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
            leaders = get_leaders(employees)

            print("Organization structure:")

            if not leaders:
                print("There are no leaders in the organization.")
            else:
                print(f" - Leaders:")
                for leader in leaders:
                    print(f"  - {leader.name} {leader.surname}")
                    if not leader.departments:
                        print("    This leader has no department.")
                    else:
                        print("   - Departments:")
                        for department in leader.departments:
                            print(f"    - {department.name}")

            if not departments:
                print("You need at least one department to show organization structure.")
            else:
                for department in departments:
                    print(f" - Department: {department.name}")
                    print(f"  - Manager: {department.manager.name} {department.manager.surname}")

                    if not department.employees:
                        print("  - There are no employees in this department.")
                    else:
                        print("  - Employees:")
                        for employee in department.employees:
                            print(f"   - {employee.name} {employee.surname}")

                    if not department.teams:
                        print("  - There are no teams in this department.")
                    else:
                        print("  - Teams:")
                        for team in department.teams:
                            print(f"   - {team.name}")

                            if not team.members:
                                print("    - There are no members in this team.")
                            else:
                                print("    - Members:")
                                for member in team.members:
                                    print(f"     - {member.name} {member.surname}")
            pause()

        elif choice == "11":
            name = get_non_empty_input("Enter a name: ")
            surname = get_non_empty_input("Enter a surname: ")
            position = get_non_empty_input("Enter a position: ")            

            while True:
                try:
                    salary = int(input("Enter a salary: "))
                    new_leader = Leader(name, surname, position, salary)
                except ValueError:
                    print("Salary must by a number and higher than 0!")
                    continue
                break

            employees.append(new_leader)
            save_employees(employees)
            save_log(f"{new_leader} created.")
            print(f"New leader with ID: {new_leader.employee_id} name: {new_leader.name}, surname: {new_leader.surname}, position: {new_leader.position}, salary: {new_leader.salary} created.")
            pause()

        elif choice == "12":

            leaders = get_leaders(employees)

            if not leaders:
                print("There are no leaders.")
            else:
                if not departments:
                    print("You need to create a department before adding to leader.")
                    
                else:
                    chosen_leader = select_employee(leaders)
                    
                    chosen_department = select_department(departments)
                    
                    try:
                        chosen_leader.add_department(chosen_department)
                    except ValueError as error:
                        print(error)
                    else:
                        save_departments(departments)
                        print(f"Department {chosen_department.name} was added to leader {chosen_leader.name} {chosen_leader.surname}")
            pause()

        elif choice == "13":
            leaders = get_leaders(employees)
            if not leaders:
                print("There are no leaders.")
            else:
                chosen_leader = select_employee(leaders)
                decision = get_non_empty_input("Decision: ")
                chosen_leader.record_decision(decision)
                print(f"Leader ID: {chosen_leader.employee_id}, {chosen_leader.name} {chosen_leader.surname} recorded decision: {decision}")
                pause()

        elif choice == "14":
            print("The program is over")
            break

        else:
            print("Invalid choice, please choose 1 - 14.")
            pause()