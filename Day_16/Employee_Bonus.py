class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def calculate_bonus(self):
        if self.salary >= 30000:
            bonus = self.salary * 10/100
            
        else:
            bonus = self.salary * 5/100
            
        final_salary = bonus + self.salary
            
            
        print("Name:", self.name)
        print("Salary: ", self.salary)
        print("Bonus Amount: ", bonus)
        print("Final Net Salary: ", final_salary)
        
        
s1 = Employee("Ravi", 29000)
s2 = Employee("Roshani", 45000)


s1.calculate_bonus()
print()

s2.calculate_bonus()