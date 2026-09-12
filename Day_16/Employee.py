class Employee:

    def __init__(self, name, employee_id, salary, department):
        self.name =name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display(self):
        print("Name: ", self.name)
        print("Employee Id: ", self.employee_id)
        print("Salary: " ,self.salary)
        print("Department: " ,self.department)

employee1 = Employee("Rohit", 101, 50000, "Compliance" )
employee2 = Employee("Sahil", 201, 50000, "Linux" )
employee3 = Employee("Rani", 301, 60000, "Development" )
employee4 = Employee("Mohit", 401, 40000, "Compliance" )

employee1.display()
print()
employee2.display()
print()
employee3.display()
print()
employee4.display()