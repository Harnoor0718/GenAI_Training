# class Test:
#     def _init_(self):
#         print(id(self))

# t = Test()
# print(id(t))

# class Test:
#     def __init__(self):
#         #instance variable
#         self.a = 10
#         self.b = 20
# t = Test()
# print(t.a)

# print(t.__dict__) # is a keyword which is used to access class attributes


# class Test:
#     def __init__(self):
#         #instance variable
#         self.a = 10
#         self.b = 20

#         #instance method can access instance variable
#     def add(self):
#         self.a + self.b
# t = Test()

# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password

#     def login(self):
#         if self.name == 'Harnoor' and self.password == 123:
#             print("Valid User")
#         else:
#             print("Invalid User")

# name = input("Enter name")
# password = int(input("Enter Password"))

# u = User(name, password)
# u.login()
        

# class, const, instance v, instance m

# Real Time Application using class and object

# class Customer:
#     bname = "SBI Bank"

#     def __init__(self, name, balance = 0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amt):
#         self.balance = self.balance + amt
#         print("After Deposit Balance is :", self.balance)

#     def withdraw(self, amt):
#         if self.balance < amt:
#             print("Insufficient Balance")

#         else:
        
#             self.balance = self.balance - amt
#             print("After Withdrawal, Balance is:", self.balance)

# name = input("Enter your name : ")
# c = Customer(name)
# print("Welcome to",Customer.bname, name )

# while True:
#     print("d-Deposit")
#     print("w-withdraw")
#     print("e-exit")

#     ch = input("Enter your choice")
#     if ch == 'd' or ch == 'D':
#         amt = int(input("Enter amount to deposit"))
#         c.deposit(amt)
#     elif ch == 'w' or ch == 'W':
#         amt = int(input("Enter amount to withdraw"))
#         c.withdraw(amt)
#     elif ch == 'e' or ch == "E":
#         print("Thanks for using SBI Mobile Banking")
#         break
#     else:
#         print("Invalid choice")

# how to delete a variable
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

    def m2(self):
        self.d = 40
        self.e = 50

        del self.a
        del self.d

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
t.m2()
print(t.__dict__)



class Grade:
    s1 = "English"
    s2 = "Hindi"
    s3 = "Punjabi"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    
    def addMarks(self):
        self.marks[self.s1] = int(input("Enter English marks: "))
        self.marks[self.s2] = int(input("Enter Hindi marks: "))
        self.marks[self.s3] = int(input("Enter Punjabi marks: "))

    
    def viewMarks(self):
        print("\nStudent Name:", self.name)
        print("English:", self.marks[self.s1])
        print("Hindi:", self.marks[self.s2])
        print("Punjabi:", self.marks[self.s3])

    
    def totalMarks(self):
        total = sum(self.marks.values())
        print("Total Marks:", total)

    
    def percentage(self):
        total = sum(self.marks.values())
        percentage = total / 3
        print("Percentage:", percentage, "%")

    
    def calculateGrade(self):
        percentage = sum(self.marks.values()) / 3

        if percentage >= 90:
            print("A+")
        elif percentage >= 80:
            print("A")
        elif percentage >= 70:
            print("B")
        elif percentage >= 60:
            print("C")
        elif percentage >= 50:
            print("D")
        else:
            print("FAIL")

        

name = input("Enter Student Name: ")

student = Grade(name, {})

while True:
    print("\n===== GRADE MANAGEMENT SYSTEM =====")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Total Marks")
    print("4. Percentage")
    print("5. Calculate Grade")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student.addMarks()

    elif choice == 2:
        student.viewMarks()

    elif choice == 3:
        student.totalMarks()

    elif choice == 4:
        student.percentage()

    elif choice == 5:
        student.calculateGrade()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")


        

