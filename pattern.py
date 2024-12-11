# n = 4
# for i in range(n,0,-1):
#     print("* "*i)
# print()

# i = 5
# while(i!=0):
#     print("* "*i)
#     i-=1

n = 4
i = 0
while(i <= n):
    s = 1
    while(s <= i):
        print(' ' , end='')
        s+=1

    j=n
    while(j > i):
        print("* ",end='')
        j-=1
    print()
    i+=1