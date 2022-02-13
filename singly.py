class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            temp = self.root
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)
            
    def print(self):
        temp = self.root
        
        while temp:
            print(temp.data) 
            temp = temp.next
   
                    
root = Node(10)        
llist = SinglyLinkedList()
llist.add(20)
llist.add(30)
llist.add(40)
llist.add(50)

# call print
# llist.print()

def reverseList(root):
    if root is None:
        return root
    if root.next is None:
        return root
    
    newNode = reverseList(root.next)
    root.next.next = root
    root.next = None
        
    return newNode
    
# call
test = reverseList(llist.root)
# print(test.data)

while(test):
    print(test.data)
    test = test.next