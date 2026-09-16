# a = int(input("Enter No:"))
# b = float(input("Enter No:"))
# c = input("Enter statement")

# a = 34
# b = 56

# temp = a
# a = b
# b = temp

# print(a," ", b)

# c = 23
# d = 78

# c = c + d
# d = c - d
# c = c - d

# print(c," ", d)


# m1 = int(input("Enter English Marks:"))
# m2 = int(input("Enter Maths Marks:"))
# m3 = int(input("Enter Science Marks:"))
# m4 = int(input("Enter SST Marks:"))

# avg = (m1 + m2 + m3 + m4) / 4


# # Rule Based 
# if avg >= 90:
#     print("Grade A")
# elif avg >= 80:
#     print("Grade B")
# elif avg >= 70:
#     print("Grade C")
# elif avg >= 60:
#     print("Grade D")
# elif avg >= 50:
#     print("Grade E")
# else:
#     print("FAIL")



# for i in range(5):
#     print(i)

# for i in range(1, 21, 2):
#     print(i)

# roll_no = [2, 3, 4, 5, 6]
# name = ["Amit", "Rohit", "Sahil", "Ramesh", "Suresh"]
# course = ["Python", "Java", "C++", "C#", "JavaScript"]

# for r, n, c in zip(roll_no, name, course):
#     print(r, n, c)

# sum = 0
# mul = 1

# for i in range(1, 6):
#     sum += i
#     mul *= i

# print(sum)
# print(mul)

# for i in range(1, 22):
#     if i % 2 == 0:
#         print(i)

# n = int(input("Enter No:"))

# n1 = 0
# n2 = 1

# for i in range(n):
#     print(n1, end=" ")
    # n3 = n1 + n2
    # n1 = n2
    # n2 = n3

# Reverse no using while loop
# Armstrong no using while loop
# prime no 
# palindrome no using while loop

# Reverse the digits of a number
# a = 678
# b = 0

# while a > 0:
#     r = a % 10          
    
#     b = b * 10 + r      
#     a = a // 10         

# print("\nReversed number:", b)


# a = 153
# sum = 0
# while a > 0:
#     r = a % 10
#     sum = sum + (r ** 3)

#     a = a // 10

# if sum == 153:
#     print("Armstrong No")
# else:
#     print("Not Armstrong No")


# a = 29
# for i in range(2, int(a**0.5) + 1):
#     if a % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")


a = 123454321

n = a
b = 0

while a > 0:
    r = a % 10          
    
    b = b * 10 + r      
    a = a // 10  

if n == b:
    print("Palindrome No")
else:
    print("Not Palindrome No")







