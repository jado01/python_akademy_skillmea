from models.employee import Employee
from models.organization import Manager, Department, Leader
from services.data_storage import (
    DATA_FILE,
    ORGANIZATION_FILE,
    save_departments,
    save_employees
    )


def create_demo_data():
    if DATA_FILE.exists() or ORGANIZATION_FILE.exists():
        print("Demo data were not created because data files already exist.")
        return

    it_manager = Manager(
        "Peter", "Novak", "IT Manager", 3200
    )
    hr_manager = Manager(
        "Maria", "Kovacova", "HR Manager", 3000
    )

    operations_leader = Leader(
        "Juraj", "Horvath", "Operations Director", 4200
    )
    unassigned_leader = Leader(
        "Anna", "Mala", "Strategy Director", 4000
    )

    it_employee_1 = Employee(
        "Martin", "Hruby", "Python Developer", 2400
    )
    it_employee_2 = Employee(
        "Lucia", "Vesela", "System Administrator", 2300
    )
    hr_employee_1 = Employee(
        "Jana", "Siroka", "Recruiter", 1900
    )
    hr_employee_2 = Employee(
        "Michal", "Mokry", "HR Specialist", 2000
    )

    employees = [
        it_manager,
        hr_manager,
        operations_leader,
        unassigned_leader,
        it_employee_1,
        it_employee_2,
        hr_employee_1,
        hr_employee_2,
    ]

    it_department = Department("IT", it_manager)
    hr_department = Department("HR", hr_manager)

    departments = [it_department, hr_department]

    operations_leader.add_department(it_department, log_event=False)
    operations_leader.add_department(hr_department, log_event=False)

    it_department.add_employee(it_employee_1, log_event=False)
    it_department.add_employee(it_employee_2, log_event=False)
    hr_department.add_employee(hr_employee_1, log_event=False)
    hr_department.add_employee(hr_employee_2, log_event=False)

    development_team = it_department.create_team("Development")
    infrastructure_team = it_department.create_team("Infrastructure")
    recruitment_team = hr_department.create_team("Recruitment")
    hr_department.create_team("Payroll")

    development_team.add_member(it_employee_1)
    development_team.add_member(it_employee_2)
    infrastructure_team.add_member(it_employee_2)
    recruitment_team.add_member(hr_employee_1)
    recruitment_team.add_member(hr_employee_2)

    save_employees(employees)
    save_departments(departments)

    print("Demo data were created successfully.")
    print("Run main.py to explore the application.")
    

if __name__ == "__main__":
    create_demo_data()
