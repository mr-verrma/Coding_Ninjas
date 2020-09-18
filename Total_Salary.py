## Read input as specified in the question.
## Print output as specified in the question.

N= input().strip().split(' ')

basic= int(N[0])
grade=N[1]

hra = 0.20 * basic
da = 0.50 * basic
pf = 0.11 * basic

allow=0
if grade == 'A':
    allow = 1700
elif grade == 'B':
    allow = 1500
else:
    allow = 1300

totalSalary = basic + hra + da+ allow -pf

print(round(totalSalary)) #round is used for round off the value