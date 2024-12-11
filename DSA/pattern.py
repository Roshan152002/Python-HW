# https://github.com/fkilld/js-and-dsa/blob/main/azad%20dsa/2%20Patterns%201/2.3.%20Patterns%202.ipynb

row = 4
col = 4


# 1st pattern
# * * *
# * * *
# * * *

# i = 1
# while(i<=row):
#     j = 1
#     while (j <= col):
#         print("* " , end='')
#         j+=1
#     print()
#     i+=1

# 2nd pattern
# 1111
# 2222
# 3333
# 4444

# i = 1
# while(i<=row):
#     j = 1
#     while (j <= col):
#         print(f'{i}' , end='')
#         j+=1
#     print()
#     i+=1


# 3rd pattern
# 1234
# 1234
# 1234
# 1234

# i = 1
# while(i<=row):
#     j = 1
#     while (j <= col):
#         print(f'{j}' , end='')
#         j+=1
#     print()
#     i+=1

# 4th pattern
# 4321
# 4321
# 4321
# 4321

# i = 1
# while(i<=row):
#     j = col
#     while (j > 0):
#         print(f'{j}' , end='')
#         j-=1
#     print()
#     i+=1

# # 5th pattern
# 1
# 12
# 123
# 1234

# i = 1
# while(i<=row):
#     j = 1
#     while (j <= i):
#         print(f'{j}' , end='')
#         j+=1
#     print()
#     i+=1


# 6th pattern
# 1
# 23
# 345
# 4567

# i = 1
# while(i<=row):
#     j = 1
#     k = i
#     while (j <= i):
#         print(f'{k}' , end='')
#         j+=1
#         k+=1
#     print()
#     i+=1

# i = 1
# while(i<=row):
#     j = 1
#     k = i
#     while (j <= i):
#         print(f'{k}' , end='')
#         j+=1
#         k+=1
#     print()
#     i+=1

# 7th pattern
# 1
# 23
# 456
# 78910

# i = 1
# k = 1
# while(i<=row):
#     j = 1
#     while (j <= i):
#         print(f'{k}',end='')
#         j+=1
#         k+=1
#     print()
#     i+=1

# 8th pattern
# 1 
# 11 
# 202 
# 3003 
# 40004

i = 1
while (i<=row):
    j = 1
    while(j <= i):
        if i == 2 :
            print(f'1',end='')
        elif j == 1 or j == i:
            print(f'{i}',end='')
        else:
            print('0',end='')
        j+=1
    print()
    i+=1