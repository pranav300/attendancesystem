n=7
fact=1
if n < 0:
    print("Factorial not possible")
elif n==0:
    print("The factorial of 0 = 1")
else:

        for i in range(1,n+1):
            fact*=i;
        print("The factorial of ",n," is: ",fact)

