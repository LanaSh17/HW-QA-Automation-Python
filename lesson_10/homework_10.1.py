class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        self.programming_language = programming_language
        self.team_size = team_size


# Тест на наявність атрибутів TeamLead

def test_teamlead_attributes():
    teamlead = TeamLead(
        "Oleksandr",
        10000,
        "Development",
        "Python",
        5
    )

    assert hasattr(teamlead, "name")
    assert hasattr(teamlead, "salary")
    assert hasattr(teamlead, "department")
    assert hasattr(teamlead, "programming_language")
    assert hasattr(teamlead, "team_size")


test_teamlead_attributes()

print("Test passed!")