class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def get_salary(self):
        return self.salary

    @get_salary.setter
    def set_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self.salary = value


emp = Employee(50000)
print(emp.get_salary)  # Accessing salary using getter
emp.set_salary = 60000  # Setting salary using setter
# emp.set_salary = -1  # Attempting to set a negative salary (will raise ValueError)
print(emp.get_salary)
