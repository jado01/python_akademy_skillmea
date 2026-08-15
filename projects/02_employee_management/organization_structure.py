from helpers import clear_terminal, pause


def print_organization_structure(employees, departments):
    clear_terminal()

    widths = (20, 22, 22, 22, 17, 22)

    def person_name(person):
        if person is None:
            return "none"
        return f"{person.name} {person.surname}"

    def print_row(
        department,
        leader,
        manager,
        employee,
        team,
        member,
    ):
        print(
            f"| {department:<{widths[0]}} | "
            f"{leader:<{widths[1]}} | "
            f"{manager:<{widths[2]}} | "
            f"{employee:<{widths[3]}} | "
            f"{team:<{widths[4]}} | "
            f"{member:<{widths[5]}} |"
        )

    print("ORGANIZATION STRUCTURE\n")

    if not departments:
        print("There are no departments to show. Create a department first.")

    else:
        header = (
            f"| {'Department':<{widths[0]}} | "
            f"{'Leader':<{widths[1]}} | "
            f"{'Manager':<{widths[2]}} | "
            f"{'Dept. employee':<{widths[3]}} | "
            f"{'Team':<{widths[4]}} | "
            f"{'Team member':<{widths[5]}} |"
        )

        separator = "-" * len(header)

        print(separator)
        print(header)
        print(separator)

        for department in departments:
            employee_names = []

            for employee in department.employees:
                employee_names.append(person_name(employee))

            if not employee_names:
                employee_names.append("none")

            team_rows = []

            if department.teams:
                for team in department.teams:
                    if not team.members:
                        team_rows.append((team.name, "none"))
                    else:
                        for number, member in enumerate(team.members):
                            if number == 0:
                                team_name = team.name
                            else:
                                team_name = ""

                            team_rows.append((team_name, person_name(member)))
            else:
                team_rows.append(("none", ""))

            row_count = max(len(employee_names), len(team_rows))

            for row_number in range(row_count):
                if row_number == 0:
                    department_name = department.name
                    leader_name = person_name(department.leader)
                    manager_name = person_name(department.manager)
                else:
                    department_name = ""
                    leader_name = ""
                    manager_name = ""

                if row_number < len(employee_names):
                    employee_name = employee_names[row_number]
                else:
                    employee_name = ""

                if row_number < len(team_rows):
                    team_name, member_name = team_rows[row_number]
                else:
                    team_name = ""
                    member_name = ""

                print_row(
                    department_name,
                    leader_name,
                    manager_name,
                    employee_name,
                    team_name,
                    member_name
                )

            print(separator)

    unassigned_leaders = []

    for employee in employees:
        if employee.employee_type == "leader" and not employee.departments:
            unassigned_leaders.append(employee)

    if unassigned_leaders:
        print("\nLeaders without an assigned department:")

        for leader in unassigned_leaders:
            print(f"  - {person_name(leader)}")

    print()
    pause()
