class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age: ",self.age)

student1 = Student("Roshani" , 22)
student2 = Student("Prerna", 21)

student1.display()
student2.display()


        
