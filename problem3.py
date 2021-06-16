n=1000
power=2
result=1
for i in range(n):
    result=result*power
copy=result
add=0
while(copy):
    digit=copy%10
    add=add+digit
    copy=copy//10
print(add)
