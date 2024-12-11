# Q1 . Write a Python program to print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print(i,end=' ')


# Q2. Use a for loop to print the even numbers between 1 and 20.

# for i in range(1,21):
#     if i%2==0:
#         print(i,end=' ')

# Q3 . Write a for loop to calculate the sum of numbers from 1 to 50.

# sum = 0
# for i in range(1,51):
#     sum = sum + i 
# print(f'sum of 50 numbers is {sum}')

# Q4 .Create a for loop to print each character of the string "Hello World".

# s = 'Hello World'

# for i in s:
#     print(i)

# Q5 . Write a program that uses a for loop to print the multiplication table of 5.

# for i in range(1,11):
#     print(f'5 * {i} = {5*i}')

# Q6 . Write a for loop to find the factorial of a number (e.g., 5!).

# n = 10
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f'the factorial of {n} is {fact}')

# Q7 . Use a for loop to iterate through a list of integers and count how many are greater than 50.

# l = [28 , 18 , 67 ,37 , 843, 382 , 76]

# count = 0
# for i in l:
#     if i > 50 :
#         count += 1 # count = count + 1
# print(f"the total count is {count} greater than 50")       

# Q8 Write a program to print all prime numbers between 1 and 50 using a for loop.

# n = int(input('enter no:'))

# for i in range(1,n+1):
#     is_prime = True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime = False
#             break
#     if is_prime :
#         print(i , end=' ')

# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count == 2:
#     print('prime no')
# else:
#     print('no')
        
# class Person:
#     species = "Homo sapiens"  # Class variable

#     def __init__(self, name, age):
#         self.name = name  # Instance variable
#         self.age = age    # Instance variable

# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)


# print(person1.species)  # Output: Homo sapiens
# print(person2.species)  # Output: Homo sapiens


# tup = (1,[1,3,4],(1,3),{'a':0})
# print(tup[3][0])  # Output: (1,)  # Note the trailing comma
# print(type(tup))
# tup[1][0]=10
# print(tup)  # Output: 1

# str = 'hello'
# list1 = list(str)
# set1 = list(set(list1))
# d = {}
# print(list1)
# print(set1)

# for i in set1:
#     count = 0 
#     for j in list1:
#         if i == j:
#             count+=1
#     d[i] = count

# print(d)


# def check_palindrome(s):
#     return s[:]==s[::-1]

# print(check_palindrome('nitin'))

a = 10,20,30
print(type(a))
print(a)