### Python Data Types
# 1. Check the Type: Write a program to take an input from the user and print its data type.

# var = input('Enter the any type of value :')
# print(type(var))


# 2. Simple Arithmetic: Accept two numbers from the user and perform addition, subtraction, multiplication, and division.

# a = float(input("Enter 1st number:"))
# b = float(input("Enter 2nd number:"))

# print(f'Addition = {a+b}')
# print(f'Substration = {a-b}')
# print(f'Multiplication = {a*b}')
# print(f'Division = {a/b}')

# 3. Temperature Converter: Convert a given temperature from Celsius to Fahrenheit and vice versa

# print('1. Fahrenheit to Celsius')
# print('2. Celsius to Fahrenheit')

# choice = int(input('Enter your choice: '))

# if choice ==  1:
#     fahrenheit = float(input('Enter temperature in Fahrenheit: '))
#     celsius = (fahrenheit - 32) * 5.0/9.0
#     print(f'{fahrenheit}°F = {celsius}°C')
# else : 
#     celsius = float(input('Enter temperature in Celsius: '))
#     fahrenheit = (celsius * 9.0/5.0) + 32
#     print(f'{celsius}°C = {fahrenheit}°F')


### Condition Flow
# 4. Even or Odd: Write a program that checks if a number entered by the user is even or odd.

# num = int(input('Enter the number:'))

# if num % 2 == 0:
#     print('Number is EVEN')
# else:
#     print('Number is ODD')


# 5. Vowel or Consonant: Accept a character from the user and determine whether it is a vowel or a consonant.

# char = input("Enter the character:")

# char = char.lower()

# if char in 'aeiou':
#     print("ITs an VOWEL")
# else:
#     print("ITs a CONSONANT")

# 6. Grade Calculator: Input a percentage and output a grade according to the following:
#    - 90-100: A
#    - 80-89: B
#    - 70-79: C
#    - 60-69: D
#    - Below 60: F

# marks =  int(input('Enter the marks:'))

# if marks >= 90:
#     print('Grade A')
# elif marks >=80:
#     print('Grade B')
# elif marks>=70:
#     print('Grade C')
# elif marks>=60:
#     print('Grade D')
# else:
#     print('FAIL')



### Lists
# 7. Sum of Elements: Write a program to calculate the sum of all elements in a list.

# l = list(map(int,input('Enter the list elements:').split()))

# sum = 0

# for i in l:
#     sum += i

# print(sum)

# 8. Largest Number: Find the largest number in a list without using built-in functions.

# l = list(map(int,input('Enter the list elements:').split()))

# print(max(l)) # using built-in function

# maxx = l[0]

# for i in range(1,len(l)):
#     if maxx < l[i]:
#         maxx = l[i]

# print(f'the maximum number is {maxx}')


# 9. Reverse a List: Reverse a given list without using built-in methods.

# l = list(map(int,input('Enter the list elements:').split()))

# reverse = l[::-1]

# print(f'Reverse list :{reverse}')


# 10. Remove Duplicates: Write a program to remove duplicates from a list.

# l = list(map(int,input('Enter the list elements:').split()))

# unique = list(set(l))

# print(unique)


### Dictionaries
# 11. Key Checker: Write a program to check if a given key exists in a dictionary.

# dictionary = {
#     "name": "Roshan",
#     "age": 22,
#     "city": "Udgir",
#     "country": "INDIA"
# }

# key = input("Enter the key you want to check:")

# if key in dictionary:
#     print('Key Exits !!')
# else:
#     print('Key NOT Exits !!')

# 12. Merge Dictionaries: Combine two dictionaries into one.

# dictionary1 = {
#     "name": "Roshan",
#     "age": 22,
#     "city": "Udgir",
#     "country": "INDIA"
# }

# dictionary2 = {
#     'profession':'data analyst',
#     'salary':50000
# }

# for key , value in dictionary2.items():
#     dictionary1[key] = value

# print(dictionary1)

# 13. Frequency Counter: Count the frequency of each character in a given string and store it in a dictionary.


# word = input('Enter the word:')

# frequency = {}

# l = list(word)
# s = list(set(l))

# for i in s:
#     count = 0
#     for j in l:
#         if i == j :
#             count+=1
#     frequency[i] = count

# print(frequency)

# d = {
#     'santosh':84,
#     'rohit': 89,
#     'roshan':88,
#     'samiksha':90,
#     'sameer':57
# }
# maximum = 0
# for key , value in d.items():
#     if maximum < d[key] :
#         maximum = d[key]

# print(maximum)


### For Loops
# 15. Factorial: Write a program to calculate the factorial of a given number using a for loop.

# n = int(input("Enter the Number:"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f'the factorial of {n} is {fact}')

# 16. Multiplication Table: Print the multiplication table of a number entered by the user.

# num = int(input("Enter the number to Print the Table:"))

# for i in range(1,11):
#     print(f'{num} * {i} = {num*i}')

# 17. Sum of Squares: Calculate the sum of squares of the first N natural numbers.

# num = int(input("ENter the number:"))

# sum = 0
# for i in range(1,num+1):
#     sum = sum + i**2

# print(sum)


### While Loops
# 18. Guess the Number: Implement a number-guessing game where the user has to guess a number between 1 and 100. Provide feedback ("Too High" or "Too Low") until they guess correctly.

# import random

# num = random.randint(1,100)

# while True:
#     guess_num = int(input('Enter guess:'))
#     if num == guess_num:
#         print("You Guess Correctly !! you won .")
#         break
#     elif guess_num > num :
#         print('TOO HIGH .')
#     else:
#         print('TOO LOW . ')


# 19. Reverse Digits: Write a program to reverse the digits of a number using a while loop.

num = int(input('Enter the number:'))

# reverse = num[::-1]
# print(reverse)

rev = 0
while num != 0:
    r = num % 10
    num = num // 10
    rev = (rev * 10) + r
print(rev)

# 20. Fibonacci Series: Generate the first N Fibonacci numbers using a while loop.

num = int(input('Enter the limit:'))


first_num = 0
second_num = 1
next_num = 0

i = 0
while i < num:
    if i == 0:
        print(first_num , end=' ')
    elif i == 1:
        print(second_num, end=' ')
    else:
        next_num = first_num + second_num
        print(next_num,end=" ")
        first_num = second_num
        second_num = next_num
    i+=1