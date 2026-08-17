import unittest
from models.employee import Employee
from models.organization import Department, Leader, Manager, Team


class TestEmployee(unittest.TestCase):
    def test_employee_rejects_zero_salary(self):
        with self.assertRaises(ValueError):
            Employee("Test", "Employee", "Tester", 0)

    def test_employee_is_created_with_valid_salary(self):
        employee = Employee("Juraj", "Siroky", "Tester", 1500)
        self.assertEqual(employee.salary, 1500)

    def test_employee_rejects_zero_salary_increase(self):
        employee2 = Employee("Janko", "Mrkvicka", "Tester", 1600)
        with self.assertRaises(ValueError):
            employee2.raise_salary(0)

class TestDepartment(unittest.TestCase):
    def test_manager_cannot_manage_two_departments(self):
        manager = Manager("Juraj", "Zatko", "Manager", 2000)
        department = Department("IT", manager)
        with self.assertRaises(ValueError):
            Department("HR", manager)

    def test_employee_cannot_be_added_to_two_departments(self):
        manager = Manager("Frantisek", "Suchy", "Manager", 2100)
        manager2 = Manager("Alica", "Zazracna", "Manager", 2100)
        department = Department("IT", manager)
        department2 = Department("HR", manager2)
        employee = Employee("Martin", "Hruby", "Tester", 1800)

        department.add_employee(employee, log_event=False)

        with self.assertRaises(ValueError):
            department2.add_employee(employee)

    def test_department_rejects_duplicate_team_name(self):
        manager = Manager("Janko", "Hrasko", "Manager", 2100)
        department = Department("IT", manager)
        department.create_team("Testing")

        with self.assertRaises(ValueError):
            department.create_team("testing")
        