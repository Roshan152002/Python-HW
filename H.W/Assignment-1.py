# Q1 Check a number
# Write a program to check if a number is positive, negative, or zero.


n = int(input("Enter the number:"))

if n > 0:
    print("The number you have entered is POSITIVE !")
elif n < 0:
    print("The number you have entered is NEGATIVE !")
else:
    print("The number you have entered is ZERO !")


# Q2 Check even or odd
# Write a program to check if a given number is even or odd.

n = int(input("Enter a number:"))

if n%2==0 :
    print("EVEN !")
else:
    print("ODD !")


# Q3 Grade Checker
#  Write a program to display grades based on a percentage:
# A: 90-100
# B: 70-89
# C: 50-69
# F: Below 50

marks = int(input("Enter your percentage:"))

if  marks >= 90 and marks < 100:
    print("Grade: A")

elif  marks >=70 and marks < 90 :
    print("Grade : B")

elif marks >=50 and marks < 70 :
    print("Grade : C")

else:
    print("Grade : F")


# Q4 Check divisibility
#  Check if a given number is divisible by 3, 5, or both.

n = int(input("ENter the number:"))

if n % 3 == 0 and n % 5 == 0:
    print("Number is divisible by 3 and 5 !")

elif n % 3 == 0 :
    print("Number is divisible by 3 !")

elif n%5 == 0:
    print("Number is divisible by  5 !")

else:
    print("THe number is not divisible 3 and 5 ")

# Q5Minimum of two numbers
#  Find the smaller number between two given numbers

n1 = int(input("Enter the 1st number:"))
n2 = int(input("Enter the 2nd number:"))

if n1 < n2:
    print("n1 is smaller than n2")
else:
    print("n2 is smaller than n1")


# Q6 Find the largest of three numbers
#  Given three numbers, find the largest using nested if statements.

x  = int(input("Enter the number:"))
y  = int(input("Enter the number:"))
z  = int(input("Enter the number:"))

if x > y :
    if  x > z:
        print(f"{x} is the largest number")
if y > x :
    if y > z:
        print(f"{y} is the largest number")
else:
    print(f"{z} is the largest number")


# Q7 Check leap year
#  Write a program to check if a given year is a leap year or not:
# Divisible by 4 and not 100, or divisible by 400.


year = int(input('Enter your year:'))

if year % 4 ==0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


# Q8 Nested temperature check
#  Categorize temperature into:
# Cold: Below 15°C
# Warm: 15°C to 30°C
# Hot: Above 30°C

temperature = int(input("Enter the temperature:"))

if temperature >= 30 :
    print("HOT")
elif temperature >=15 and temperature < 30:
    print("WARM")
else:
    print("COLD")

# Q9 Vowel or consonant
#  Check if a given character is a vowel or consonant.


char = input('Enter charcter:')

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("vowel")
else:
    print("consonant")


# Q10 Must be 18 or older.
# Nested check for possessing a valid license.

age = int(input('Enter your age:'))
license = input('Do you have a valid license:')

if age >= 18:
    if license == 'yes':
        print('You are eligible to drive')
    else:
        print('You are not eligible to drive')
else:
    print('You are not eligible to drive')


# Q11 Triangle validation
# Check if three sides can form a triangle:
# The sum of any two sides must be greater than the third side.


a = int(input('Enter the first side:'))
b = int(input('Enter the second side:'))
c = int(input('Enter the third side:'))

if a + b > c and a + c > b and b + c > a:
    print('The sides can form a triangle')
else:
    print('The sides cannot form a triangle')


# Q12 Calculate tax based on salary
#  Determine the tax rate:
# Salary ≤ 5,00,000: 5%
# 5,00,001 - 10,00,000: 10%
# Above 10,00,000: 20%

salary = int(input('Enter you salary to calculate tax:'))

if salary <= 500000:
    print(f'tax on {salary} is {salary*0.05}')

elif salary >= 500001 and salary < 1000000:
    print(f'tax on {salary} is {salary*0.1}')

else:
    print(f'tax on {salary} is {salary*0.2}')



# Q13 Categorize age
#  Categorize a person's age:
# 0-12: Child
# 13-19: Teen
# 20-59: Adult
# 60+: Senior

age = int(input('Enter your age: '))
if age <= 12:
    print('You are a child')
elif age >= 13 and age <= 19:
    print('You are a teen')
elif age >= 20 and age <= 59:
    print('You are an adult')
else:
    print('You are a senior')


# Q14 Logical AND check
#  Check if a number is greater than 10 and divisible by 2.   

num = int(input('Enter a number: '))
if num > 10 and num % 2 == 0:
    print('The number is greater than 10 and divisible by 2')
else:
    print('The number is not greater than 10 or not divisible by 2')


#Q15 Logical OR check
#  Check if a number is less than 5 or greater than 20.

num = int(input('Enter a number: '))
if num < 5 or num > 20:
    print('The number is less than 5 or greater than 20')
else:
    print('The number is between 5 and 20')


# Q16 Electricity bill
#  Calculate an electricity bill:
# Usage ≤ 100 units: ₹5/unit
# 101-200 units: ₹10/unit
# Above 200 units: ₹15/unit

usage = int(input("Enter your electricity usage in unit:"))

if usage <= 100:
    print(f"Your electricity bill is {usage*5} Rs")
elif usage >= 101 and usage < 200:
    n = usage - 100
    print(f"Your electricity bill is {(n*10) + (100*5)} Rs")
else:
    n = usage - 200
    print(f"Your electricity bill is {(n*15) + (100*5) + (100*10)} Rs")


#Q 17. Season finder  
# Find the season based on the month:
# - December-February: Winter
# - March-May: Spring
# - June-August: Summer
# - September-November: Autumn

month = input('Enter the month:')

if month in ['December', 'January', 'February']:
    print('Winter')
elif month in ['March','April','May']:
    print('Spring')
elif month in ['June','July','August']:
    print('Summer')
else:
    print('Autumn')



# Q18 Password validation
#  Check if a password meets these conditions:
# At least 8 characters.
# Contains the character '@'.

password = input('Enter password :')

if len(password) >= 8 and '@' in password:
    print('Password is valid')
    
elif len(password) < 8:
    print('Password should be 8 characters long')

elif '@' not in password:
    print("Password should contain @ character !")



# Q19.Categorize BMI
#  Categorize Body Mass Index (BMI):
# Below 18.5: Underweight
# 18.5 - 24.9: Normal
# 25 - 29.9: Overweight
# 30 or higher: Obese

BMI = float(input())

if BMI < 18.5:
    print("Underweight")

elif 18.5 >= BMI and BMI < 24.9:
    print("Normal")

elif 25 >= BMI and 29.9 > BMI:
    print("Overweight")

else:
    print('Obese')



# Q20 Character type checker
#  Check if a given character is:
# Alphabet
# Digit
# Special character

ch = input("Enter the character:")

if ch.isalpha():
    print("Alphabet")

elif ch.isdigit():
    print("Digit")

else:
    print('Special Character')

