class Student:
    
    def __init__(self, name, marks):
        self.name =name
        self.marks = marks
        
    def display (self):
        print("Student name:", self.name)
        print("Student Marks:", self.marks)
        
student1  = Student("Ravi" , 91 )
student2  = Student("Roshani", 92)

student1.display()

print()

student2.display()