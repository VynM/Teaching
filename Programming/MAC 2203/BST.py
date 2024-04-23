class BST:
    nil = True
    
    def isNil(self):
        return self.nil
    
    def __init__(self, val = None):
        if val:
            self.insert(val)
            
    def inorder(self):
        if not self.isNil():
            return self.left.inorder() + " " + str(self.val) + " " + self.right.inorder()
        else:
            return ""
        
    def insert(self, val):
        if self.isNil():
            self.nil = False
            self.val = val
            self.left = BST()
            self.right = BST()
            self.parent = BST()
            
        elif val < self.val:
            self.left.insert(val)
            self.left.parent = self
        else:
            self.right.insert(val)
            self.right.parent = self
            
    def find(self, val):
        if self.isNil():
            raise Exception(str(val) + " does not exist in the tree")
        elif val < self.val:
            return self.left.find(val)
        elif val > self.val:
            return self.right.find(val)
        else:
            return self
        
    def minimum(self):
        if self.isNil():
            raise Exception("Tree is empty")
        elif self.left.isNil():
            return self
        else:
            return self.left.minimum()
        
    def maximum(self):
        if self.isNil():
            raise Exception("Tree is empty")
        elif self.right.isNil():
            return self
        else:
            return self.right.maximum()        
        
    def successor(self, x):
        if not x.right.isNil():
            return x.right.minimum()
        y = x.parent
        while not y.isNil() and x == y.right:
            x = y
            y = y.parent
        return y
    

t = BST()
for x in [10, 35, 20, 50, 90, 4, 100, 10, 90, 3, 300, 20]:
    t.insert(x)
    
print(t.inorder())

print("\nMinimum: ", t.minimum().val)
print("Maximum: ", t.maximum().val, "\n")

            