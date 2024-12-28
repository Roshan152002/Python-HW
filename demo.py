# # lst = [1, 2, 4, 5]
# # n = max(lst)
# # expected_sum = n * (n + 1) // 2
# # actual_sum = sum(lst)
# # missing_number = expected_sum - actual_sum
# # print("Missing Number:", missing_number)

# # n = len(lst) + 1

# # for i in range(1,n+1):
# #     if i not in lst:
# #         print("Missing Number:", i)


# # class Father:
# #     def money_and_land(self):
# #         # self.name = 'xyz'
# #         print("Father has money and land")

# #     def money(self):
# #         self.name='lal singh chadda'
        

# # class Son(Father):
# #     # def __init__(self):

# #     def money(self):
# #         # self.name='abc'
# #         print("Son has money")

# # s = Son()
# # s.money()
# # print(s.name)

# class A:
#     def show(self):
#         print("welcome")

#     def show(self,firstname):
#         print("welcome",firstname)

#     def show(self,firstname='',lastname=''):
#         print("welcome",firstname,lastname)


# a = A()

# a.show('roshan')

# # Question: Write a Python function to generate the Fibonacci sequence up 
# # to the Nth number. 

# # def fibo(n):
# #     fibo_series = [0,1]
# #     if n <= 0:
# #         return []
# #     elif n <= 1:
# #         return [0]
# #     else:
# #         while(len(fibo_series) < n):
# #             fibo_series.append(fibo_series[-1]+fibo_series[-2])

# #     return fibo_series           

# # n = int(input('Enter nth number:'))
# # print(fibo(n))

# # def check_palindrome(s):
# #     S = s.lower()
# #     return S == S[::-1]

# # print(check_palindrome('Nitin'))


# # def second_largest(l):
# #     new = list(set(l))
# #     new.sort(reverse=True)
# #     return new[1] if len(l) > 1 else None

# # l = [1,8734,24738,2,4,6,42,3]
# # print(second_largest(l))


# s = 'hello'

# set1 = set(s)
# print(set1)  # {'h', 'l', 'o', 'e'}


# print(1 ,end=' ')
# print(1 ,end=' ')
# print(1 ,end=' ')

# l = list([1,2,3,4])
# print(l.index(3))
# print(l)

# l = [1,3,-1,5,6]

# for i in l:
#     if i < 0:
#         l.insert(-1,i)
        
# print(l)



l = dict(name ='roshan',age=22)
print(l)