n=100
product=1
for i in range(1,n+1):
    product = product * i
copy=product
add=0
while(copy):
    digit=copy%10
    add=add+digit
    copy=copy//10
print(add)
