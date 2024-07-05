class AVLNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1  

    def __str__(self):
        return f"AVLNode(data={self.data}, height={self.height})"

if __name__ == "__main__":
 
    node1 = AVLNode(10)
    node2 = AVLNode(20)
    node3 = AVLNode(5)

   
    node1.left = node3
    node1.right = node2
    node3.parent = node1
    node2.parent = node1

    
    print(node1)  
    print(node2)  
    print(node3) 
