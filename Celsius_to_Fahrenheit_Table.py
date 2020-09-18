start=int(input())
end=int(input())
step=int(input())

while(start<=end):
    currFah = start
    cel = (9/5)*(currFah-32)
    print(currFah+ "\t" + cel)
    currFah+=step