# Employee and Team Management System

A command-line application for managing employees, managers, leaders, departments, and teams.

The project demonstrates object-oriented programming, inheritance, composition, validation, JSON data persistence, audit logging, and automated model tests. It was created as the second main project of the Skillmea Python Academy.

## Features

- Create employees, managers, and leaders with unique IDs.
- Validate salaries and increase an employee's salary.
- Create departments and assign managers.
- Add employees to departments and teams.
- Create multiple teams within a department.
- Assign departments to leaders.
- Record leader decisions in the audit log.
- Display employees and departments in formatted tables.
- Display the complete organization structure in a single overview.
- Save and restore application data using JSON files.
- Generate ready-to-use demo data.
- Verify core domain rules with automated tests.

## Business Rules

The application enforces several relationships between its objects:

- A manager can manage only one department.
- An employee can belong to only one department.
- A department can have only one leader.
- A leader can manage multiple departments.
- An employee can join multiple teams within their department.
- An employee cannot be added to the same team more than once.
- Department and team names cannot be empty or duplicated within the same scope.

## Requirements

- Python 3
- No third-party packages are required.

## Running the Application

Clone the repository and open the project directory:

```bash
git clone https://github.com/jado01/python_akademy_skillmea.git
cd python_akademy_skillmea/projects/02_employee_management
```

Start the application:

```bash
python main.py
```

The application presents an interactive menu divided into employee, department, team, and organization management sections.

## Demo Data

To explore a populated application without entering all records manually, run:

```bash
python demo_data.py
```

The script creates a small organization containing employees, managers, leaders, departments, teams, and team memberships. It does not overwrite existing application data. If either data file already exists, the script stops and displays a warning.

After generating the demo data, start the application and choose **Show organization structure** to see the complete overview:

```bash
python main.py
```

## Running the Tests

Run the automated test suite from the project directory:

```bash
python -m unittest discover -s tests -v
```

The tests currently verify:

- rejection of a zero starting salary,
- creation of an employee with a valid salary,
- rejection of a zero salary increase,
- prevention of one manager managing two departments,
- prevention of one employee joining two departments,
- prevention of duplicate team names within a department.

## Data Persistence and Logging

Application data is stored locally in the `data` directory:

- `employees.json` stores employees, managers, and leaders.
- `organization_structure.json` stores departments, relationships, teams, and team memberships.
- `employee_management.log` stores timestamped audit events.

The generated data and log files are excluded from Git, so each user works with their own local data.

## Project Structure

```text
02_employee_management/
|-- main.py                    # Application entry point
|-- menu.py                    # Main interactive menu
|-- actions.py                 # Menu actions and workflows
|-- helpers.py                 # Input, selection, and terminal helpers
|-- organization_structure.py # Formatted organization overview
|-- demo_data.py               # Optional demo data generator
|-- models/
|   |-- employee.py            # Employee model and salary validation
|   `-- organization.py        # Manager, Leader, Department, and Team models
|-- services/
|   |-- data_storage.py        # JSON persistence
|   `-- audit_log.py           # Audit logging
`-- tests/
    `-- test_models.py         # Automated model tests
```

## Concepts Practised

- classes and objects,
- encapsulation and properties,
- inheritance and method overriding,
- composition and relationships between objects,
- validation and exception handling,
- file handling and JSON serialization,
- audit logging,
- refactoring and separation of responsibilities,
- automated testing with `unittest`.

## Project Background

This project was developed as the second main assignment of the Skillmea Python Academy. Its purpose is to practise building a larger application step by step, connecting multiple object-oriented models, persisting their relationships, and gradually refactoring the code into a clearer project structure.
