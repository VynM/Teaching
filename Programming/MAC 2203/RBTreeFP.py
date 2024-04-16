from dataclasses import dataclass
from enum import Enum

class Color(Enum):
    B = 0
    R = 1

def colStr(col: Color):
    return "B" if col == Color.B else "R"

class Tree:
    col: Color
    
class E:
    col = Color.B
    
    def __repr__(self):
        return ""
     
@dataclass
class T:
    col: Color
    left: Tree
    val: int
    right: Tree
    
    def __repr__(self):
        return "(" + str(self.left) + ")<-" + colStr(self.col) + str(self.val) + "->(" + str(self.right) + ")"
    
def isEmpty(t):
    match t:
        case E():
            return True
        case _:
            return False
        
def isIn(t, x):
    match t:
        case E():
            return False
        case T(_, left, val, right):
            if x == val:
                return True
            elif x < val:
                return isIn(left, x)
            else:
                return isIn(right, x)
            
def makeBlack(t):
    match t:
        case T(_, left, val, right):
            return T(Color.B, left, val, right)
        
def balance(col, t1, z, t2):
    match (col, t1, z, t2):
        case (Color.B, T(Color.R, T(Color.R, a, x, b), y, c), z, d):
            return T(Color.R, T(Color.B, a, x, b), y, T(Color.B, c, z, d))
        case (Color.B, T(Color.R, a, x, T(Color.R, b, y, c)), z, d):
            return T(Color.R, T(Color.B, a, x, b), y, T(Color.B, c, z, d))
        case (Color.B, a, x, T(Color.R, b, y, T(Color.R, c, z, d))):
            return T(Color.R, T(Color.B, a, x, b), y, T(Color.B, c, z, d))
        case (Color.B, a, x, T(Color.R, T(Color.R, b, y, c), z, d)):
            return T(Color.R, T(Color.B, a, x, b), y, T(Color.B, c, z, d))
        case _:
            return T(col, t1, z, t2)

def ins(t, x):
    match t:
        case E():
            return T(Color.R, E(), x, E())
        case T(col, l, y, r):
            if x < y:
                return balance(col, ins(l, x), y, r)
            elif x > y:
                return balance(col, l, y, ins(r, x))
            else:
                return t

def insert(t, x):
    return makeBlack(ins(t, x))

        
t = E()

for x in [60, 20, 50, 100, 30, 75, 3, 10, 27]:
    t = insert(t, x)
    
print(t)
        
        
        
        
        
        
        
        
        
        