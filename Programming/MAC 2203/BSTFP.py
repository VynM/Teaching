from dataclasses import dataclass

class BST:
    isNil: bool
    
class Nil(BST):
    isNil = True
    
    def __str__(self):
        return ""
    
@dataclass
class Node(BST):
    val: int
    left: BST
    right: BST
    
    def __str__(self):
        return "(" + str(self.left) + ")<-" + str(self.val) + "->(" + str(self.right) + ")"
    
def isInTree(tree: BST, x: int):
    match tree:
        case Nil():
            return False
        case Node(val, left, right):
            if x == val:
                return True
            elif x < val:
                return isInTree(left, x)
            else:
                return isInTree(right, x)

def inorder(tree):
    match tree:
        case Node(val, left, right):
            inorder(left)
            print(val)
            inorder(right)

def insert(tree, x):
    match tree:
        case Nil():
            return Node(x, Nil(), Nil())
        case Node(val, left, right):
            if x < val:
                return Node(val, insert(left, x), right)
            else:
                return Node(val, left, insert(right, x))
    
def minTree(tree):
    match tree:
        case Node(_, Nil(), _):
            return tree
        case Node(_, left, _):
            return minTree(left)

def delete(tree, x):
    match tree:
        case Nil():
            return tree
        case Node(val, left, right):
            if x < val:
                return Node(val, delete(left, x), right)
            elif x > val:
                return Node(val, left, delete(right, x))
            else:
                match (left, right):
                    case (Nil(), _):
                        return right
                    case (_, Nil()):
                        return left
                    case _:
                        rmin = minTree(right)
                        return Node(rmin.val, left, delete(right, rmin.val))
                        
        
t = Nil()
for x in [60, 20, 50, 100, 30, 75, 3, 10, 27]:
    t = insert(t, x)
    
print(t)

for x in [3, 100, 27, 60, 20, 75, 10, 50, 30]:
    t = delete(t, x)
    print(t)
