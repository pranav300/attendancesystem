n=4
stare=""
for i in range(0,n):
    for j in range (0,n):
        if i<=j:
            stare=stare+'*'

    print(stare)
    stare=""