from helpers import clear_terminal, pause, get_non_empty_input, get_leaders
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
            print("Salary must be a number greater than 0.")
            continue
        break

    employees.append(new_employee)
    save_employees(employees)
    save_log(f"{new_employee} created.")
    print(f"\nEmployee created successfully:\n"
          f"  ID: {new_employee.employee_id}\n"
          f"  Name: {new_employee.name} {new_employee.surname}\n"
          f"  Position: {new_employee.position}\n"
          f"  Salary: {new_employee.salary}\n"
    )
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
            entered_id = int(input("\nEnter employee ID: "))
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
                            print("\nAmount must be a number greater than 0.")
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
            print("Salary must be a number greater than 0.")
            continue
        break

    employees.append(new_manager)
    save_employees(employees)
    save_log(f"{new_manager} created.")
    print(f"\nManager created successfully:\n"
          f"  ID: {new_manager.employee_id}\n"
          f"  Name: {new_manager.name} {new_manager.surname}\n"
          f"  Position: {new_manager.position}\n"
          f"  Salary: {new_manager.salary}\n"
    )
    pause()

def create_department(employees, departments):
    clear_terminal()
    managers = []

    for employee in employees:
        if employee.employee_type == "manager" and employee.managed_department is None:
            managers.append(employee)

    if not managers:
        print("There are no available managers.\n"
              "Create a new manager before creating a department.\n"
        )
        pause()
        return

    print("\nFirst, select an available manager for the new department.\n"
          "\nAvailable managers:\n"
    )
    
    for manager in managers:
        print(f"  ID {manager.employee_id} | {manager.name} {manager.surname} | {manager.position}")

    found_manager = None

    while True:
        try:
            manager_id = int(input("\nEnter manager ID: "))
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
                    print("This department already exists. Please try again.")
                else:
                    new_department = Department(department_name, found_manager)
                    departments.append(new_department)
                    save_departments(departments)
                    print("\nDepartment created successfully:\n\n"
                          f"  Name: {new_department.name}\n"
                          f"  Manager: {found_manager.name} {found_manager.surname}"
                    )
                    print()
                    break
            break
    pause()

def show_departments(departments):
    clear_terminal()
    if not departments:
        print("No departments to show.")
    else:
        print("\nAll departments:\n")
        print(
            f"{'No.':<5}"
            f"{'Department':<26}"
            f"{'Manager':<28}"
            f"{'Employees':>12}"
            f"{'Teams':>8}"
        )
        print("-" * 79)

        for number, department in enumerate(departments, start=1):
            full_name = f"{department.manager.name} {department.manager.surname}"

            print(
                f"{number:<5}"
                f"{department.name:<26}"
                f"{full_name:<28}"
                f"{len(department.employees):>12}"
                f"{len(department.teams):>8}"
            )
        print()
    pause()

def add_employee_to_department(employees, departments):
    clear_terminal()
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
            print("First, select the department where the employee will be added.\n")
            found_department = select_department(departments)

            print(f"\nSelect an employee to add to department {found_department.name}.\n")

            while True:
                chosen_employee = select_employee(available_employees)

                try:
                    found_department.manager.add_employee_to_department(found_department, chosen_employee)
                    save_departments(departments)
                except ValueError as error:
                    print(error)
                else:
                    print(f"\nEmployee {chosen_employee.name} {chosen_employee.surname}"
                          f" added to department {found_department.name}\n"
                    )
                    break
    pause()

def create_team(departments):
    clear_terminal()
    if not departments:
        print("\nYou need to create a department before creating a team.\n")
    else:
        print("\nFirst, select the department where the new team will be created.\n")
        found_department = select_department(departments)

        while True:
            team_name = get_non_empty_input("Enter the team name: ")
            try:
                new_team = found_department.create_team(team_name)
            except ValueError as error:
                print(error)
            else:
                save_departments(departments)
                print(f"\nTeam created successfully:\n\n"
                      f"  Name: {new_team.name}\n"
                      f"  Department: {found_department.name}"
                      )
                print()
                print(found_department.list_teams())
                print()
                break
    pause()

def add_employee_to_team(departments):
    clear_terminal()

    if not departments:
        print("You need at least one department.")
    else:
        print("\nFirst, select a department to add one of its employees to a team.\n")
        found_department = select_department(departments)

        if not found_department.teams:
            print(f"Department {found_department.name} has no teams.")
        else:

            if not found_department.employees:
                print(f"Department {found_department.name} has no employees.")
            else:
                print("\nNow select the team where the employee will be added.\n")
                found_team = select_team(found_department)
                available_employees = []

                for employee in found_department.employees:
                    if employee not in found_team.members:
                        available_employees.append(employee)

                if not available_employees:
                    print("There are no available employees to add to this team.")

                else:
                    print(f"\nNow select an employee from department {found_department.name}"
                          f" to add to team {found_team.name}.\n"
                    )
                    chosen_employee = select_employee(available_employees)

                    try:
                        found_department.add_employee_to_team(chosen_employee, found_team)
                    except ValueError as error:
                        print(error)
                    else:
                        save_departments(departments)
                        print("\nEmployee added to team successfully:\n\n"
                            f"  Employee: {chosen_employee.name} {chosen_employee.surname}\n"
                            f"  Department: {found_department.name}\n"
                            f"  Team: {found_team.name}\n"
                        )
                        print(found_team.list_members())
                        print()
    pause()

def create_leader(employees):
    clear_terminal()
    name = get_non_empty_input("Enter a name: ")
    surname = get_non_empty_input("Enter a surname: ")
    position = get_non_empty_input("Enter a position: ")

    while True:
        try:
            salary = int(input("Enter a salary: "))
            new_leader = Leader(name, surname, position, salary)
        except ValueError:
            print("Salary must be a number greater than 0.")
            continue
        break

    employees.append(new_leader)
    save_employees(employees)
    save_log(f"{new_leader} created.")
    print(f"\nLeader created successfully:\n\n"
          f"  ID: {new_leader.employee_id}\n"
          f"  Name: {new_leader.name} {new_leader.surname}\n"
          f"  Position: {new_leader.position}\n"
          f"  Salary: {new_leader.salary}\n"
    )
    pause()

def assign_department_to_leader(employees, departments):
    clear_terminal()
    leaders = get_leaders(employees)

    if not leaders:
        print("There are no leaders.")
    else:
        if not departments:
            print("You need to create a department before assigning one to a leader.")

        else:
            available_departments = []

            for department in departments:
                if department.leader is None:
                    available_departments.append(department)

            if not available_departments:
                print("There are no available departments to assign.\n")
            else:
                print("First, select a leader to assign a department.\n")

                chosen_leader = select_employee(leaders, "Available leaders:")

                chosen_department = select_department(available_departments)

                try:
                    chosen_leader.add_department(chosen_department)
                except ValueError as error:
                    print(error)
                else:
                    save_departments(departments)
                    print("\nDepartment assigned successfully:\n")
                    print(f"  Department: {chosen_department.name}\n"
                        f"  Leader: {chosen_leader.name} {chosen_leader.surname}\n"
                    )
    pause()

def record_leader_decision(employees):
    clear_terminal()
    leaders = get_leaders(employees)
    if not leaders:
        print("There are no leaders.")
    else:
        print("\nFirst, select the leader who will record a decision.\n")
        chosen_leader = select_employee(leaders, "Available leaders:")
        decision = get_non_empty_input("Enter the decision: ")
        chosen_leader.record_decision(decision)
        print("\nDecision recorded successfully:\n\n"
              f"  Leader: {chosen_leader.name} {chosen_leader.surname}\n"
              f"  Decision: {decision}\n"
        )
    pause()
