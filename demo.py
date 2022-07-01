class Student():
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def displaystudentdata(self):
        print(f"Student name={self.name} age={self.age} and rollno={self.rollno}")

while True:
    k=input("Enter any key to fill student data or Enter q for exit:")
    if k!='q':
        a = input("Enter Student Name: ")

        b = int(input("Enter age of student: "))

        c = int(input("Enter roll no of student: "))

        s1=Student(a,b,c)
        s1.displaystudentdata()
    else:
        print("Thanks for the service")
        break