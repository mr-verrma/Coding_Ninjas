#        1
#      23
#    345
#  4567

n=int(input())

for i in range(n):
    print(' '*(n-i-1),end="")
    for j in range(i+1):
        print(i+j+1,end="")
    print() 
