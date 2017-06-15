queue=[10]
def push(k,last):
    if last-first>=10:
        print("overflow");
    else :
        queue[last]=k;
        last+=1;
def pop(first,last):
    if first>=last:
        print("underflow");
        last=0;
        first=0;
    else:
        j=first;
        first+=1;
        return queue[j];
c=1
first=last=0
while c!=1:
    print("Enter 1 to enter in the queue");
    print("Enter 2 to retrieve from queue");
    print("Enter 3 to exit");
    c = int(input("Enter your choice: "));
    if c == 1:
        k = int(input("Enter the value to be entered into stack"));
        push(k,last);
    elif c == 2:
        print("The value popped from stack is: ", pop(first,last));
    elif c == 3:
        exit();
    elif c == 4:
        print("Wrong choice");