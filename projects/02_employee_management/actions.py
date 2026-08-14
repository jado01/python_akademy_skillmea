from helpers import pause, get_non_empty_input, get_leaders
from models.employee import Employee
from models.organization import Department, Leader, Manager
from services.data_storage import save_employees, save_departments
from services.audit_log import save_log
from helpers import select_department, select_employee, select_team

def create_employee(employees):
    name = get_non_empty_input("Enter a name: ")
    surname = get_non_empty_input("Enter a surname: ")
    position = get_non_empty_input("Enter a position: ")

    while True:
        try:
            salary = int(input("Enter a salary: "))
            new_employee = Employee(name, surname, position, salary)
        except ValueError:
            print("Salary must be a number and greater than 0!")
            continue
        break

    employees.append(new_employee)
    save_employees(employees)
    save_log(f"{new_employee} created.")
    print(f"\nEmployee created successfully:\n  ID: {new_employee.employee_id}\n  Name: {new_employee.name} {new_employee.surname}\n  Position: {new_employee.position}\n  Salary: {new_employee.salary}\n")
    pause()

def show_all_employees(employees):
    if not employees:
        print("\nThere are no employees.\n")
    else:
        print("\nAll employees:\n")
        print(
            f"{'ID':<5}"
            f"{'Type':<12}"
            f"{'Name':<25}"
            f"{'Position':<30}"
            f"{'Salary':>10}"
        )
        print("-" * 82)

        for employee in employees:
            full_name = f"{employee.name} {employee.surname}"

            print(
                f"{employee.employee_id:<5}"
                f"{employee.employee_type:<12}"
                f"{full_name:<25}"
                f"{employee.position:<30}"
                f"{employee.salary:>10}"
            )
        print()
    pause()

def increase_employee_salary(employees):
    if not employees:
        print("\nThere are no employees.\n")
    else:
        found_employee = None
        print("\nAvailable employees:\n")
        for employee in employees:
            print(f"  ID {employee.employee_id} | {employee.name} {employee.surname} | salary: {employee.salary}")
        try:
            entered_id = int(input("\nEnter ID of employee: "))
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
            print(
                "\nSelected employee:\n\n"
                f"  ID: {found_employee.employee_id}\n"
                f"  Name: {found_employee.name} {found_employee.surname}\n"
                f"  Position: {found_employee.position}\n"
                f"  Salary: {found_employee.salary}\n"
                )

            while True:
                confirmation = input(
                    "Increase the salary of this employee? (y/n): "
                    ).strip().lower()

                if confirmation == "y":
                    old_salary = found_employee.salary

                    while True:
                        try:
                            increase_amount = int(input("\nEnter the amount of the salary increase: "))
                            found_employee.raise_salary(increase_amount)
                        except ValueError:
                            print("Amount must be a number and higher then 0!")
                            continue
                        break

                    save_employees(employees)
                    print("\nSalary increased successfully:\n\n"
                        f"  Employee: {found_employee.name} {found_employee.surname}\n"
                        f"  Previous salary: {old_salary}\n"
                        f"  Increase: {increase_amount}\n"
                        f"  New salary: {found_employee.salary}\n"
                        )
                    break

                elif confirmation == "n":
                    print("\nOperation was canceled.\n")
                    break

                else:
                    print("\nInvalid input. Please enter y or n.\n")
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
    print(f"\nManager created successfully:\n  ID: {new_manager.employee_id}\n  Name: {new_manager.name} {new_manager.surname}\n  Position: {new_manager.position}\n  Salary: {new_manager.salary}\n")
    pause()

def create_department(employees, departments):
    managers = []

    for employee in employees:
        if employee.employee_type == "manager" and employee.managed_department is None:
            managers.append(employee)

    if not managers:
        print("You need at least one manager to create a new department.")
        pause()
        return
    
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

def show_departments(departments):
    if not departments:
        print("No departments to show.")
    else:
        for department in departments:
            print(f"Department: {department.name}, Manager: {department.manager.name} {department.manager.surname}")
    pause()

def add_employee_to_department(employees, departments):
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

def create_team(departments):
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

def add_employee_to_team(departments):
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

def show_organization_structure(employees, departments):
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

def create_leader(employees):
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
    print(f"\nLeader created successfully:\n  ID: {new_leader.employee_id}\n  Name: {new_leader.name} {new_leader.surname}\n  Position: {new_leader.position}\n  Salary: {new_leader.salary}\n")
    pause()

def assign_department_to_leader(employees, departments):
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

def record_leader_decision(employees):
    leaders = get_leaders(employees)
    if not leaders:
        print("There are no leaders.")
    else:
        chosen_leader = select_employee(leaders)
        decision = get_non_empty_input("Decision: ")
        chosen_leader.record_decision(decision)
        print(f"Leader ID: {chosen_leader.employee_id}, {chosen_leader.name} {chosen_leader.surname} recorded decision: {decision}")
        pause()
