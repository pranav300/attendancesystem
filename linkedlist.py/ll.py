
stack=[10]
def  push(k,to):
    if to>=10:
        print("Stack overflow");
    else:
        stack[to]=k
        to+=1


def pop(to):
    if to<0:
        print("Stack underflow");
    else:
        j=to
        to-=1
        return stack[j]
c=1;
to=0
while c!=3:
    print("Enter 1 to enter in the stack");
    print("Enter 2 to retrieve from stack");
    print("Enter 3 to exit");
    c=int(input("Enter your choice: "));
    if c==1:
        k=int(input("Enter the value to be entered into stack"));
        push(k,to);
    elif c==2:
        print("The value popped from stack is: ",pop(to));
    elif c==3:
        exit();
    elif c==4:
        print("Wrong choice");

