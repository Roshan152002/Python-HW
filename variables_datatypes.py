''' 
Variable : The variable is like container that holds the value.

Syntax : variable_name = value

constraints :
1. variable_name should be a valid python identifier.
2. variable_name should not be a keyword in python..
3. variable_name should not contain special character except underscore.
4. variable_name should not contain any space between it.

'''
# Varible Declaration.

x = 10
print(x)

'''
Datatypes : Datatype is that specifies the type of value a variable can hold.

# Type of Datatype 

There are mainly 2 types of datatypes .
1. Built-in Datatype : These are the datatypes that are already available in python.
2. User-defined Datatype : These are the datatypes that are defined by the user.

'''
# Built-in Datatype.
# Numeric: int, float, complex
# Sequence: str, list, tuple, range
# Mapping: dict
# Set Types: set, frozenset
# Boolean: bool
# Binary: bytes, bytearray, memoryview
# None Type: NoneType
'''

'''
# Integer Datatype : It is used to store integer value.

x = 10
print(type(x))

# Float Datatype : It is used to store floating point value.

x = 10.5
print(type(x))

# Complex Datatype : It is used to store complex number.
# Complex number is a number that can be expressed in the form a + bj, where a and b are real numbers and j is the imaginary unit.

x = 10 + 5j
print(type(x))

# Boolean Datatype : It is used to store boolean value.

x = True
print(type(x))

x = False
print(type(x))

# String Datatype : It is used to store string value.

x = "Hello, World!"
print(type(x))

'''
# List Datatype : 
2. List is a collection of heterogeous elements which is ordered and changeable. Allows duplicate members.
3. List is defined by placing all the elements inside square brackets [ ] separated by comma.
4. List is mutable, i.e., it can be modified after its creation.
5 .List is ordered, i.e., elements in a list have a definite order.
6. List is indexed, i.e., each element in a list has an index associated with it.
7. List is searchable, i.e., elements in a list can be searched.
8. List is sliceable, i.e., elements in a list can be sliced.
'''

x = [1, 2, 3, 4, 5]
print(type(x))

'''
# Tuple Datatype : 
1. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
2. Tuple is defined by placing all the elements inside round brackets ( ) separated by comma.
3. Tuple is immutable, i.e., it cannot be modified after its creation.
4. Tuple is ordered, i.e., elements in a tuple have a definite order.
5. Tuple is searchable, i.e., elements in a tuple can be searched.
6. Tuple is sliceable, i.e., elements in a tuple can be sliced.
'''

x = (1, 2, 3, 4, 5)
print(type(x))

'''
# Dictionary Datatype : It is used to store dictionary of value , means in the format of key value pair.
1. Dictionary is a collection which is unordered and changeable. Allows duplicate keys.
2. Dictionary is defined by placing all the elements inside curly brackets { } separated by comma.
3. Dictionary is mutable, i.e., it can be modified after its creation.
4. Dictionary is searchable, i.e., elements in a dictionary can be searched.
5. Dictionary is sliceable, i.e., elements in a dictionary can be sliced.
'''

x = {"name": "John", "age": 30, "city": "New York"}
print(type(x))

'''
# Set Datatype : 
1. Set is a similar to list but it contains the only unique values.
'''
x = {1, 2, 3, 4, 5}
print(type(x))
