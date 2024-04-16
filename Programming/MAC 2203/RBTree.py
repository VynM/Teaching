from enum import Enum

class Colour(Enum):
    Black = 0
    Red = 1
    
class Node:
    isNil = True
    colour = Colour.Black
    
    def __init__(self, val: int = None, colour: Colour = Colour.Black, left = None, right = None, parent = None):
        if val:
            self.isNil = False
            self.val = val
            self.colour = colour
            self.left = left
            self.right = right
            self.parent = parent
            
    def inorder(self):
        if self.isNil:
           return []
        else:
           return self.left.inorder() + [self.val] + self.right.inorder()
       
    def structure(self):
       if self.isNil:
           return ""
       else:
           return "(" + self.left.structure() + ")<-" + ('R' if self.colour == Colour.Red else 'B') + str(self.val) + "->(" + self.right.structure() + ")"
        
    def blackHeights(self, h = -1):
       if self.isNil:
           print(h + 1)
       else:
           self.left.blackHeights(h + 1 if self.left.colour == Colour.Black else h)
           self.right.blackHeights(h + 1 if self.right.colour == Colour.Black else h)
    
class RBTree:
    Nil = Node()  
    root = Nil
            
    def inorder(self):
        print(self.root.inorder())
        
    def structure(self):
        return self.root.structure()
        
    def insert(self, val):
        x = Node(val, colour = Colour.Red, left = self.Nil, right = self.Nil)
        y = self.Nil
        z = self.root
        
        while not z.isNil:
            y = z
            if x.val < z.val:
                z = z.left
            else:
                z = z.right
        x.parent = y
        
        if y.isNil:
            self.root = x
        elif x.val < y.val:
            y.left = x
        else:
            y.right = x
            
        self.insertFix(x)
        
    def insertFix(self, x):
        while x.parent.colour == Colour.Red:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y.colour == Colour.Red:
                    x.parent.colour = Colour.Black
                    y.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.leftRotate(x)
                    x.parent.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    self.rightRotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y.colour == Colour.Red:
                    x.parent.colour = Colour.Black
                    y.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.rightRotate(x)
                    x.parent.colour = Colour.Black
                    x.parent.parent.colour = Colour.Red
                    self.leftRotate(x.parent.parent)
        self.root.colour = Colour.Black
    
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if not y.left.isNil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent.isNil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if not y.right.isNil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent.isNil:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
    # Prints blackheights as defined along every path from the root to leaves
    def blackHeights(self):
        self.root.blackHeights()
        

t = RBTree()
for val in [50, 25, 75, 12, 1, 2, 3, 4, 100, 300, 10, 25, 15, 2]:
    t.insert(val)
    
print(t.structure())

print("Blackheights:")
t.blackHeights()