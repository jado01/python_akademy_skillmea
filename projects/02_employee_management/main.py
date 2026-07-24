from modules.employee import Employee
from modules.organization import Manager, Department, Leader

def main():
    e1 = Employee("Janko", "Mrkvicka", "Technician", 2000)
    e2 = Employee("Martina", "Vesela", "Economist", 2400)
    m1 = Manager("Martin", "Konecny", "Manager", 3000)
    d1 = Department("HR", m1)
    m2 = Manager("Peter", "Mokry", "Manager", 3100)
    d2 = Department("Tech", m2)
    l1 = Leader("Janko", "Hrasko", "Leader", 3400)

    m1.add_employee_to_department(d1, e2)
    print(d1.list_employees())
    print(d2.list_employees())
    print(l1)
    print(l1.list_departments())
    l1.add_department(d1)
    print(l1.list_departments())

if __name__ == "__main__":
    main()
