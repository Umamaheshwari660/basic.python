# i. Write a program to check if a given number is positive, negative, or zero.
num=1
if num > 0:
  print("Positive")
elif num < 0:
  print("Negative")
else:
  print("Zero")

#   ii. Determine if a number is odd or even
num=33
if num%2==0:
   print(num, "is even")
else:
   print(num, "is odd") 

#    iii. Check if a person is eligible to vote (age >= 18)
age=18
if age>=18:
   print("your eligible for vote")
else:
   print("your not eligible for vote")

#    iv. Write a program to find the greatest of two numbers.
num1=55
num2=66
if num1==num2:
    print("both are equal")
elif num1>num2:
    print(num1,"is greater")
else:
    print(num2,"is greater")

#  v. Print "Pass" if a student scores more than 40 marks;otherwise, print "Fail."   
marks=45
if marks > 40:
    print("Pass")
else:
    print("False")

# vi. Write a program to display the day of the week based on anumber input (1 for Monday, 2 for Tuesday, etc.).
day_number = 3  
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid day number")

   #  vii. Implement a simple calculator to perform addition,subtraction, multiplication, and division
num1, num2 = 10, 5  
operation = "add"  

if operation == "add":
    print("Sum:", num1 + num2)
elif operation == "subtract":
    print("Difference:", num1 - num2)
elif operation == "multiply":
    print("Product:", num1 * num2)
elif operation == "divide":
    if num2 != 0:
        print("Quotient:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

# viii. Write a program to display the name of a month based on
# the month number (1 for January, 2 for February, etc.)

month_number = 7  
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    print("Invalid month number")

   #  b. Medium Questions:
   # i. Write a program to find the greatest of three numbers.
   num1, num2, num3 = 10, 25, 15  

if num1 >= num2 and num1 >= num3:
    print("Greatest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number:", num2)
else:
    print("Greatest number:", num3)

   #  ii. Check if a year is a leap year
   year = 2024  

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

# iii. Write a program to classify a character entered by the user
# as a vowel, consonant, or neither.
char = 'a'  
char = char.lower()

if char in 'aeiou':
    print(char, "is a Vowel")
elif char.isalpha():
    print(char, "is a Consonant")
else:
    print(char, "is Neither a vowel nor a consonant")

#  iv. Calculate the grade of a student based on the marks they
# score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail   
marks = 85  

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
else:
    print("Fail")

   #  v. Write a program to check if three sides length form a valid
# triangle.
a, b, c = 3, 4, 5  

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

#  2. Loops:
# a. Easy Questions:
# i. Print all numbers from 1 to 100 using a for loop.
for i in range(1, 101):
    print(i, end=" ")  
print() 

# ii. Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2)
n = 10  
sum_n = (n * (n + 1)) // 2  
print("Sum of first", n, "natural numbers:", sum_n)


# iii. Print all even numbers between 1 and 50 using a while
# loop.
num = 2
while num <= 50:
    print(num, end=" ")
    num += 2
print() 

# iv. Write a program to display the multiplication table of a given
# number. First 20
num = 5  
for i in range(1, 21):
    print(num, "x", i, "=", num * i)

# v. Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits.
num = 1234  
reverse_num = 0
digit_sum = 0
original_num = num

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    digit_sum += digit
    num //= 10

print("Reverse of", original_num, "is", reverse_num)
print("Sum of digits of", original_num, "is", digit_sum)

# vi. Write a program to count the number of digits in a given
# number using a while loop.
num = 98765  # Example input
count = 0
temp_num = num

while temp_num > 0:
    temp_num //= 10
    count += 1

print("Number of digits in", num, "is", count)

# vii. Write a program that keeps asking the user to enter numbers
# until they enter a negative number. Use a while loop 
while True:
    user_input = int(input("Enter a number (negative to stop): "))
    if user_input < 0:
        print("Negative number entered. Exiting loop.")
        break
    else:
        print("You entered:", user_input)

#   b. Medium Questions:
# i. Print the first 10 terms of the Fibonacci series using a forloop.
print("Fibonacci Series:")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# ii. Check if a given number is a prime number using a forloop.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it is prime: "))
print(f"{num} is a prime number" if is_prime(num) else f"{num} is not a prime number")

# iii. Write a program to calculate the factorial of a number usinga while loop.
num = int(input("Enter a number to find its factorial: "))
fact = 1
i = num
while i > 1:
    fact *= i
    i -= 1
print(f"Factorial of {num} is {fact}")

# iv. Print all numbers from 1 to 100 that are divisible by 3 and 5using a for loop.
print("Numbers divisible by 3 and 5 between 1 to 100:")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print("\n")

# v. Implement a menu-driven program where the user canchoose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit.
while True:
    print("\nMenu:")
    print("1. Find the square of a number")
    print("2. Find the cube of a number")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int(input("Enter a number: "))
        print(f"Square of {num} is {num**2}")
    elif choice == 2:
        num = int(input("Enter a number: "))
        print(f"Cube of {num} is {num**3}")
    elif choice == 3:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again.")

# vi. Implement a basic login system where the user has threeattempts to enter the correct password using a loop      
correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
else:
    print("Too many failed attempts. Access denied.")