
count=0
for j in range(1,100):
    for i in range(1,j+1):
        if (j%i)==0:
            count+=1
            a=j
    if count==2:
        print(a)
    count=0