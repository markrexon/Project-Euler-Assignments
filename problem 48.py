limit=int(input("enter the limit: "))
counter=0
sum=0
for i in range(1,limit+1):
    counter=counter+1
    summing=pow(i,counter)
    sum=sum+summing
result=sum%10000000000
print(result)
