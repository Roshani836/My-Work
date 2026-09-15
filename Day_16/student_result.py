class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def result(self):
        if self.marks >= 40:
            print("Pass")
        else: 
            print("Fail")
            
    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)
        
s1 = Student("Prerna" , 80)
s2 = Student("Ravi", 35)
s3 = Student("Roshani", 85)

s1.display()
s1.result()
print()

s2.display()
s2.result()
print()

s3.display()
s3.result()
print()

    
