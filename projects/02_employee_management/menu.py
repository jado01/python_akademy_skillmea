from helpers import clear_terminal, pause, get_non_empty_input, select_department, select_employee, select_team, get_leaders
from models.organization import Department, Leader
from services.data_storage import save_employees, load_employees, save_departments, load_departments
from services.audit_log import save_log
from actions import create_employee, show_all_employees, increase_employee_salary, create_manager

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
            managers = []

            for employee in employees:
                if employee.employee_type == "manager" and employee.managed_department is None:
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
                            save_departments(departments)
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
                    if employee.employee_type == "employee" and employee.department is None:
                        available_employees.append(employee)
                if not available_employees:
                    print("There are no employees available to add.")
                else:
                    found_department = select_department(departments)                                                
                
                    print(f"Which employee do you want to add to department {found_department.name}?")

                    while True:
                        chosen_employee = select_employee(available_employees)

                        try:
                            found_department.manager.add_employee_to_department(found_department, chosen_employee)
                            save_departments(departments)
                        except ValueError as error:
                            print(error)
                        else:
                            print(f"Employee {chosen_employee.name} {chosen_employee.surname} added to department {found_department.name}")
                            break
            pause()

        elif choice == "8":
            if not departments:
                print("You need to create a department before creating a team.")
            else:
                found_department = select_department(departments)
                
                while True:
                    team_name = get_non_empty_input("Please enter a team name: ")
                    try:
                        new_team = found_department.create_team(team_name)
                    except ValueError as error:
                        print(error)
                    else:
                        save_departments(departments)
                        print(f"Team {new_team.name} was added to department {found_department.name}")
                        print(found_department.list_teams())
                        break
            pause()

        elif choice == "9":
            if not departments:
                print("You need at least one department.")
            else:
                found_department = select_department(departments)

                if not found_department.teams:
                    print(f"Department {found_department.name} has no teams.")
                else:

                    if not found_department.employees:
                        print(f"Department {found_department.name} has no employees.")
                    else:
                        found_team = select_team(found_department)
                        chosen_employee = select_employee(found_department.employees)

                        try:
                            found_department.add_employee_to_team(chosen_employee, found_team)
                        except ValueError as error:
                            print(error)
                        else:
                            save_departments(departments)
                            print(f"Employee {chosen_employee.name} {chosen_employee.surname} from department {found_department.name} was added to team {found_team.name}")
                            print(found_team.list_members())
            pause()

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