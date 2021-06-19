num=int(input("write the number:"))

value=num//2
product=1
for i in range(2,value+1):
    if num%i==0:
        product=product*i
        if product <= num:
            print(i,end=" ")
