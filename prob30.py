def seperation(num):
    sum = 0
    while(num):
        digit=num%10
        power=digit**5
        sum=sum+power
        num=num//10
    return sum
add=0

for i in range(10,1000000):
    if i==seperation(i):
        add=add+seperation(i)
print(add)
