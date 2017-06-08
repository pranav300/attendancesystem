class Node:
    def __init__(self, contents=None, next=None):
        self.contents = contents
        self.next  = next

    def getContents(self):
        return self.contents

    def __str__(self):
       return str(self.contents)

def print_list(node):
    str1="";
    while node:
        str1+=node.__str__()
        str1+="->"
        node = node.next
    print(str1)

def delete(top,node):
    node2 = top
    if node2.contents == node.contents and node2==top:
        top = top.next
        print_list(top)
        return
    prev = top
    while node2:
        node2 = node2.next
        if node2.contents == node.contents:
             prev.next = node2.next
             break
        elif node2.next==None:
            prev.next=None
            break
        prev = prev.next
    print_list(top)
    return



content=int(input("Enter the data: "))
node=top=Node(content)

for i in range(1,5):
    content=int(input("Enter the data: "))
    node1=Node(content)
    node.next=node1
    node=node.next
print_list(top)
k=int(input("Enter the position to be deleted: "))

delete(top,k)


