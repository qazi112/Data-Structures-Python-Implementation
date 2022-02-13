class TreeNode():
    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None

    
a = TreeNode(10)
b = TreeNode(20)
c = TreeNode(120)
d = TreeNode(220)
e = TreeNode(30)
f = TreeNode(40)


a.right = c
a.left = b
b.left = d
b.right = e
c.right = f



# DFSStack Traversal Tree
def satckDFS(root):
    myStack = []
    results = []
    myStack.append(root)
    
    while len(myStack) != 0:
        current = myStack.pop()
        if current:
            print(current.data)
            results.append(current.data)
            if current.left:
                myStack.append(current.left)
            if current.right:
                myStack.append(current.right)
    return results

# BFSQueue Traversal Tree
def BFSQueue(root):
    queue = []
    results = []
    
    queue.append(root)
    while(queue):
        current = queue.pop(0)
        if current:
            print(current.data)
            results.append(current.data)
            queue.append(current.left)
            queue.append(current.right)
    return results

# DFS Recursion, Find the data      
def DFS(root, data):
    if not root:
        return False
    if root.data == data:
        return True
    else:
        return DFS(root.left, data) or DFS(root.right, data)


# Find the value BFSQueueFind(root, data)
def BFSQueueFind(root, data):
    queue = []
    results = []
    status = False
    queue.append(root)
    
    while(queue):
        current = queue.pop(0)
        if current:
            current_data = current.data 
            print(current_data)
            if current_data == data:
                print("Found")
                status = True
                break
            results.append(current_data)
            queue.append(current.left)
            queue.append(current.right)
            
    return results, status


# Search data in Binary Tree using Recursion
def findDataUsingRecursion(root, data):
    if not root:
        return False

    if(root.data == data):
        return True
    
    return findDataUsingRecursion(root.right, data) or findDataUsingRecursion(root.left, data)


    

