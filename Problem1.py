n = int(input("write the number you want:"))
sum=0
for i in range(1,n):
    if (i%3==0) or (i%5==0):
        print(i)
        sum=sum+i

print("The sum of all the multiples of 3 or 5 below 1000:",sum)
