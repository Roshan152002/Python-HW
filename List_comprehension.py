# Python list comprehension:

# 1. Squares of Numbers
# Generate a list of squares for numbers from 1 to 10.

num = int(input('Enter the range till you want squares:'))

squares = [i**2 for i in range(1,num+1)]
print(squares)

# 2. Even Numbers
# Create a list of even numbers between 1 and 20.

n = int(input('Enter the range till you want even numbers:'))
even = [i for i in range(1,n+1) if i%2==0]
print(even)

# 3. Uppercase Strings
# Convert a list of strings to uppercase.

strings = input('Enter strings:').strip(' ').split()

uppercase = [strings[i].upper() for i in range(len(strings)) ]
print(uppercase)


# 4. Filter Positive Numbers
# Extract only positive numbers from a given list.

l = input('Enter list elements:').split(' ') 

positives = [int(i) for i in l if int(i) > 0]
print(positives)


# 5. Pairs of Numbers
# Generate all pairs (i, j) where i is from 1 to 3 and j is from 4 to 6.

pairs = [(i,j) for i in range(1,4)  for j in range(4,7)]
print(pairs)


# 6. Fibonacci Numbers
# Create a list of the first 10 Fibonacci numbers using list comprehension.

imit = int(input("Enter the limit :"))

fibo = [0,1] 
[fibo.append(fibo[-1] + fibo[-2])  for i in range(2,limit)] 
print(fibo)

# 7. Flatten a Matrix
# Flatten a 2D matrix into a single list.

x =  [[1, 2], [3, 4], [5, 6]]
l= []
l1 = [l.extend(x[i]) for i in range(len(x)) ]
print(l)

# Example Input: [[1, 2], [3, 4], [5, 6]]
# Example Output: [1, 2, 3, 4, 5, 6]
īīī
# 8. Length of Strings
# Generate a list of the lengths of each string in a list.

strin = input('Enter strings:').strip(' ').split()
lengths = [len(strin[i]) for i in range(len(strin))]
print(lengths)

# Example Input: ["apple", "banana", "cherry"]
# Example Output: [5, 6, 6]

# 9. Multiples of 3 or 5
# Create a list of numbers between 1 and 50 that are multiples of 3 or 5.

multiples = [i for i in range(1,51) if i % 3 == 0 or i % 5 == 0]
print(multiples)


# Example Output: [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50]

# 10. Reverse Strings
# Create a new list where each string in the input list is reversed.

s = input('Enter strings:').strip(' ').split()
reverse = [s[i][::-1] for i in range(len(s))]
print(reverse)


# Example Input: ["hello", "world", "python"]
# Example Output: ["olleh", "dlrow", "nohtyp"]