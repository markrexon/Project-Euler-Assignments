lst=[]
counter=0
for i in range(2,101):
    for j in range(2,101):
        val=i**j
        if val not in lst:
            lst.append(val)
            counter+=1

print("The no of items are ",counter)
