n=4

for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(i+j+1,end="")
    print()
for i in range(1,n):
    for j in range(i+1):
        print(i+j+1,end="")
    print()