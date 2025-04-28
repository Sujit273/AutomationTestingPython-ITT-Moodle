# # if statements
# age = 29
# if age >=18:
#     print("You are eligible for vote")
#
# #if ....else statements
# num = (int(input("Please enter a Number: ")))
# if num % 2 ==0:
#     print("Even number")
# else:
#     print("Odd number")
#
# ### if...elif...else statements
# mark = (int(input("Please enter a Mark: ")))
# if mark >= 90:
#     print("Grade: A")
# elif mark >= 75:
#     print("Grade: B")
# elif mark >= 60:
#     print("Grade: C")
# elif mark >=35:
#     print("Grade: D")
# else:
#     print("Grade: F")
#
# ### Nested if statement
# num = 20
#
# if num >20:
#     if num <30:
#         print("Number is valid")
# else:
#     print("Enter a valid number")
#
# ### Multiple Conditions Using and, or
# username = "admin"
# password = "12345"
#
# if username == "admin" and  password == "12345":
#     print("Login successful")
# else:
#     print("Invalid credentials")


#####################################################
### Q1. Check if a number is positive, negative, or zero
# num = (int(input("Enter a number: ")))
#
# if num > 0:
#     print("Number is positive.")
# elif num == 0:
#     print("Number is zero")
# else:
#     print("Number is Negative")
#
# ### Q2. Take a year and check if it is a leap year.
# year = (int(input("Enter a Year: ")))
# if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
#     print(year, " is a leap year.")
# else:
#     print(year, " is not a leap year")

### Q3. Take 3 numbers and print the largest.
num1 = 90
num2 = 78
num3 = 56

if num1 > num2 and num1 > num3:
    print("Number1 is the largest")
elif num2 > num3 and num2 > num1:
    print("Number2 is the largest")
else:
    print("Number3 is the largest")

# print("Largest number is:",max(num1,num2,num3))